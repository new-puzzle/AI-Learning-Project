# React/TypeScript Integration Guide

This guide shows how to integrate the Learning Path Generator with a React (TypeScript) + Vite frontend.

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│   React/TypeScript Frontend (Vite)  │
│   - User input forms                │
│   - Learning path display           │
│   - AI chat interface               │
└──────────────┬──────────────────────┘
               │ HTTP API calls
               ▼
┌─────────────────────────────────────┐
│   Python Backend API (FastAPI)      │
│   - generator.py                    │
│   - ai_chat.py                      │
│   - scheduler.py                    │
└─────────────────────────────────────┘
```

## 📋 Setup Steps

### 1. Create Python API Backend

Create a FastAPI backend that wraps the generator:

```python
# api_server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from generator import LearningPathGenerator
from ai_chat import AIChatAssistant

app = FastAPI()

# Enable CORS for React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize generators
generator = LearningPathGenerator()
chat_assistant = AIChatAssistant()

# Request/Response models
class LearningPathRequest(BaseModel):
    topic: str
    timeframe: int
    hours_per_day: float
    start_date: Optional[str] = None
    skip_weekends: bool = False
    skip_weekdays: Optional[List[int]] = None
    unavailable_dates_input: Optional[str] = None
    proficiency: Optional[str] = None
    focus_areas: Optional[List[str]] = None
    additional_requests: Optional[str] = None

class ChatMessage(BaseModel):
    message: str
    conversation_history: Optional[List[dict]] = None

class ChatResponse(BaseModel):
    response: str

# API Endpoints
@app.post("/api/generate-path")
async def generate_learning_path(request: LearningPathRequest):
    """Generate a learning path"""
    try:
        path = generator.generate_learning_path(
            topic=request.topic,
            timeframe=request.timeframe,
            hours_per_day=request.hours_per_day,
            start_date=request.start_date,
            skip_weekends=request.skip_weekends,
            skip_weekdays=request.skip_weekdays,
            unavailable_dates_input=request.unavailable_dates_input,
            proficiency=request.proficiency,
            focus_areas=request.focus_areas,
            additional_requests=request.additional_requests
        )
        return path
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
async def chat(request: ChatMessage):
    """AI chat endpoint"""
    try:
        response = chat_assistant.chat(
            request.message,
            conversation_history=request.conversation_history
        )
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/suggest-learning")
async def suggest_learning_path(goal: str, current_skills: Optional[str] = None):
    """Get learning suggestions"""
    try:
        response = chat_assistant.suggest_learning_path(goal, current_skills)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 2. Install Python Dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 3. Run the API Server

```bash
python api_server.py
```

The API will run on `http://localhost:8000`

## ⚛️ React/TypeScript Frontend

### 1. Install Dependencies

```bash
npm install axios
# or
yarn add axios
```

### 2. Create API Client

```typescript
// src/services/api.ts
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export interface LearningPathRequest {
  topic: string;
  timeframe: number;
  hours_per_day: number;
  start_date?: string;
  skip_weekends?: boolean;
  skip_weekdays?: number[];
  unavailable_dates_input?: string;
  proficiency?: string;
  focus_areas?: string[];
  additional_requests?: string;
}

export interface LearningPath {
  overview: string;
  milestones: string[];
  curriculum: CurriculumDay[];
  metadata: {
    topic: string;
    timeframe: number;
    hours_per_day: number;
    [key: string]: any;
  };
}

export interface CurriculumDay {
  day: number;
  topic: string;
  learning_objectives: string[];
  estimated_hours: number;
  priority: string;
  due_date?: string;
  resources: Resource[];
}

export interface Resource {
  type: string;
  name: string;
  url: string;
}

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

export const api = {
  // Generate learning path
  generateLearningPath: async (request: LearningPathRequest): Promise<LearningPath> => {
    const response = await axios.post(`${API_BASE_URL}/generate-path`, request);
    return response.data;
  },

  // Chat with AI
  chat: async (message: string, history: ChatMessage[] = []): Promise<string> => {
    const response = await axios.post(`${API_BASE_URL}/chat`, {
      message,
      conversation_history: history
    });
    return response.data.response;
  },

  // Get learning suggestions
  suggestLearning: async (goal: string, currentSkills?: string): Promise<string> => {
    const response = await axios.post(`${API_BASE_URL}/suggest-learning`, null, {
      params: { goal, current_skills: currentSkills }
    });
    return response.data.response;
  },

  // Health check
  health: async (): Promise<{ status: string }> => {
    const response = await axios.get(`${API_BASE_URL}/health`);
    return response.data;
  }
};
```

### 3. Create Learning Path Generator Component

```typescript
// src/components/LearningPathGenerator.tsx
import { useState } from 'react';
import { api, LearningPathRequest, LearningPath } from '../services/api';

export default function LearningPathGenerator() {
  const [formData, setFormData] = useState<LearningPathRequest>({
    topic: '',
    timeframe: 30,
    hours_per_day: 2.0,
    skip_weekends: false,
  });
  const [loading, setLoading] = useState(false);
  const [path, setPath] = useState<LearningPath | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const result = await api.generateLearningPath(formData);
      setPath(result);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to generate learning path');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="learning-path-generator">
      <h2>Generate Learning Path</h2>
      
      <form onSubmit={handleSubmit}>
        <div>
          <label>Topic</label>
          <input
            type="text"
            value={formData.topic}
            onChange={(e) => setFormData({ ...formData, topic: e.target.value })}
            placeholder="e.g., prompt engineering, n8n"
            required
          />
        </div>

        <div>
          <label>Timeframe (days)</label>
          <input
            type="number"
            value={formData.timeframe}
            onChange={(e) => setFormData({ ...formData, timeframe: parseInt(e.target.value) })}
            min={1}
            max={365}
            required
          />
        </div>

        <div>
          <label>Hours per day</label>
          <input
            type="number"
            step="0.5"
            value={formData.hours_per_day}
            onChange={(e) => setFormData({ ...formData, hours_per_day: parseFloat(e.target.value) })}
            min={0.5}
            max={24}
            required
          />
        </div>

        <div>
          <label>
            <input
              type="checkbox"
              checked={formData.skip_weekends}
              onChange={(e) => setFormData({ ...formData, skip_weekends: e.target.checked })}
            />
            Skip weekends
          </label>
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Generating...' : 'Generate Path'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}

      {path && (
        <div className="learning-path-result">
          <h3>Overview</h3>
          <p>{path.overview}</p>

          <h3>Milestones</h3>
          <ul>
            {path.milestones.map((milestone, i) => (
              <li key={i}>{milestone}</li>
            ))}
          </ul>

          <h3>Curriculum</h3>
          {path.curriculum.map((day) => (
            <div key={day.day} className="curriculum-day">
              <h4>Day {day.day}: {day.topic}</h4>
              <p>Hours: {day.estimated_hours}</p>
              <ul>
                {day.learning_objectives.map((obj, i) => (
                  <li key={i}>{obj}</li>
                ))}
              </ul>
              <div>
                <strong>Resources:</strong>
                {day.resources.map((resource, i) => (
                  <a key={i} href={resource.url} target="_blank" rel="noopener noreferrer">
                    {resource.name}
                  </a>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

### 4. Create AI Chat Component

```typescript
// src/components/AIChat.tsx
import { useState } from 'react';
import { api, ChatMessage } from '../services/api';

export default function AIChat() {
  const [message, setMessage] = useState('');
  const [history, setHistory] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;

    const userMessage: ChatMessage = { role: 'user', content: message };
    const newHistory = [...history, userMessage];
    setHistory(newHistory);
    setMessage('');
    setLoading(true);

    try {
      const response = await api.chat(message, history);
      setHistory([...newHistory, { role: 'assistant', content: response }]);
    } catch (error) {
      console.error('Chat error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ai-chat">
      <h2>AI Learning Advisor</h2>
      
      <div className="chat-messages">
        {history.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <strong>{msg.role === 'user' ? 'You' : 'AI'}:</strong>
            <p>{msg.content}</p>
          </div>
        ))}
        {loading && <div>AI is thinking...</div>}
      </div>

      <form onSubmit={handleSend}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about learning, career, skills..."
        />
        <button type="submit" disabled={loading}>Send</button>
      </form>
    </div>
  );
}
```

### 5. Use in Your App

```typescript
// src/App.tsx
import LearningPathGenerator from './components/LearningPathGenerator';
import AIChat from './components/AIChat';

function App() {
  return (
    <div className="app">
      <h1>Learning Path Generator</h1>
      <AIChat />
      <LearningPathGenerator />
    </div>
  );
}

export default App;
```

## 🚀 Running the Full Stack

### Terminal 1: Python API
```bash
cd standalone_learning_generator
python api_server.py
```

### Terminal 2: React App
```bash
cd your-react-app
npm run dev
```

## 📝 Notes

- The Python backend handles all AI logic
- React frontend just makes HTTP requests
- You can customize the UI components as needed
- The API is RESTful and easy to extend
- CORS is configured for local development

## 🔧 Customization

- Modify `api_server.py` to add more endpoints
- Customize React components to match your design
- Add authentication if needed
- Deploy backend separately (e.g., Railway, Render, AWS)
- Deploy frontend to Vercel, Netlify, etc.

