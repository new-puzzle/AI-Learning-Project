# Standalone Learning Path Generator

> **👋 START HERE!** This is the main entry point. Read this file first.

This folder contains extracted components from the AI Learning Project that you can use in your React/TypeScript app (or any frontend) to generate detailed learning paths for topics like "prompt engineering" or "n8n".

## 📁 Files Overview

### Core Modules (Framework-Agnostic)
- **`generator.py`** - Main generator class for creating learning paths
- **`ai_chat.py`** - AI chat assistant for learning suggestions
- **`ai_prompts.py`** - AI prompt generation logic
- **`scheduler.py`** - Date scheduling utilities (weekends, weekdays, unavailable dates)

### Backend API (For React/TypeScript)
- **`api_server.py`** - FastAPI backend server ⭐ **Use this for React apps**

### Documentation
- **`REACT_INTEGRATION.md`** - Complete React/TypeScript integration guide
- **`ARCHITECTURE.md`** - Component structure and data flow (optional read)
- **`example_usage.py`** - Python code examples

### Optional (Streamlit Only)
- **`input_form.py`** - Streamlit UI components (not needed for React)

---

## 🚀 Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 2. For React/TypeScript Apps (Recommended)

**Step 1:** Start the Python API server:
```bash
python api_server.py
```
Server runs on `http://localhost:8000`

**Step 2:** In your React app, call the API:
```typescript
import axios from 'axios';

const response = await axios.post('http://localhost:8000/api/generate-path', {
  topic: "prompt engineering",
  timeframe: 30,
  hours_per_day: 2.0,
  skip_weekends: true
});
```

**📖 See [REACT_INTEGRATION.md](REACT_INTEGRATION.md) for complete guide with React components.**

### 3. Python Usage (Direct)

```python
from generator import LearningPathGenerator

# Initialize
generator = LearningPathGenerator(api_key="your-api-key")

# Generate learning path
path = generator.generate_learning_path(
    topic="prompt engineering",
    timeframe=30,
    hours_per_day=2.0,
    skip_weekends=True
)

print(path['overview'])
print(f"Total days: {len(path['curriculum'])}")
```

---

## 💬 AI Chat Assistant

Get AI suggestions on what to learn before generating a path:

### Python Usage

```python
from ai_chat import AIChatAssistant

assistant = AIChatAssistant(api_key="your-api-key")

# Get learning suggestions
response = assistant.suggest_learning_path(
    goal="become an AI engineer",
    current_skills="I know Python basics"
)
print(response)

# Regular chat
response = assistant.chat("What should I learn to master prompt engineering?")
print(response)

# Compare topics
response = assistant.compare_topics(
    topic1="prompt engineering",
    topic2="n8n automation"
)
print(response)
```

### Via API (React)

```typescript
// Chat endpoint
const response = await axios.post('http://localhost:8000/api/chat', {
  message: "What should I learn to become an AI engineer?",
  conversation_history: [] // Optional
});

// Learning suggestions
const suggestions = await axios.post('http://localhost:8000/api/suggest-learning', {
  goal: "become a prompt engineer",
  current_skills: "I know Python basics"
});
```

**Available Methods:**
- `chat(message, conversation_history)` - General chat
- `suggest_learning_path(goal, current_skills)` - Get learning suggestions
- `compare_topics(topic1, topic2, context)` - Compare two topics

---

## 📋 Learning Path Generator

### Input Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `topic` | str | ✅ | Topic to learn (e.g., "prompt engineering") |
| `timeframe` | int | ✅ | Number of days (1-365) |
| `hours_per_day` | float | ✅ | Hours per day (0.5-24) |
| `start_date` | str | ❌ | Start date (YYYY-MM-DD) |
| `skip_weekends` | bool | ❌ | Skip weekends (default: False) |
| `skip_weekdays` | list | ❌ | Weekdays to skip (0=Mon, 6=Sun) |
| `unavailable_dates_input` | str | ❌ | Dates to skip (e.g., "Nov 20-22") |
| `proficiency` | str | ❌ | Beginner/Intermediate/Advanced |
| `focus_areas` | list | ❌ | Specific areas to focus on |
| `additional_requests` | str | ❌ | Additional preferences |

### Scheduling Examples

**Weekdays only:**
```python
skip_weekends=True
```

**Weekends only:**
```python
skip_weekdays=[0,1,2,3,4]  # Skip Mon-Fri
```

**Custom days:**
```python
skip_weekdays=[2, 4]  # Skip Wed & Fri
unavailable_dates_input="Dec 24-26, Jan 1"  # Skip holidays
```

### Output Structure

```python
{
    "overview": "2-3 sentence summary",
    "milestones": [
        "Day X: Achievement description",
        ...
    ],
    "curriculum": [
        {
            "day": 1,
            "topic": "Topic name",
            "learning_objectives": ["Objective 1", ...],
            "estimated_hours": 2.0,
            "priority": "high",
            "due_date": "2025-01-01",  # If start_date provided
            "resources": [
                {
                    "type": "video",
                    "name": "Resource name",
                    "url": "https://..."
                },
                ...
            ]
        },
        ...
    ],
    "metadata": {
        "topic": "...",
        "timeframe": 30,
        "hours_per_day": 2.0,
        ...
    }
}
```

---

## 💡 Example Use Cases

### Weekend Learner
```python
path = generator.generate_learning_path(
    topic="n8n automation",
    timeframe=60,
    hours_per_day=4.0,
    skip_weekdays=[0,1,2,3,4],  # Only weekends
    start_date="2025-01-04"
)
```

### Weekday Evening
```python
path = generator.generate_learning_path(
    topic="prompt engineering",
    timeframe=30,
    hours_per_day=1.5,
    skip_weekends=True,
    unavailable_dates_input="Dec 24-26"
)
```

### With Focus Areas
```python
path = generator.generate_learning_path(
    topic="Machine Learning",
    timeframe=60,
    hours_per_day=3.0,
    proficiency="Intermediate",
    focus_areas=[
        "Neural Networks",
        "Deep Learning",
        "Model Deployment"
    ],
    additional_requests="Focus on practical projects"
)
```

---

## 🔧 API Endpoints (FastAPI)

When running `api_server.py`, these endpoints are available:

- `POST /api/generate-path` - Generate learning path
- `POST /api/chat` - AI chat
- `POST /api/suggest-learning` - Get learning suggestions
- `POST /api/compare-topics` - Compare two topics
- `GET /api/health` - Health check
- `GET /docs` - Interactive API documentation (Swagger UI)

---

## 🔑 API Key Setup

**Option 1: Environment Variable**
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

**Option 2: Windows PowerShell**
```powershell
$env:ANTHROPIC_API_KEY="your-key-here"
```

**Option 3: Direct Parameter**
```python
generator = LearningPathGenerator(api_key="your-key-here")
```

---

## 📦 Dependencies

```txt
anthropic>=0.18.0
fastapi>=0.104.0      # For api_server.py
uvicorn[standard]>=0.24.0  # For api_server.py
pydantic>=2.0.0       # For api_server.py
streamlit>=1.28.0     # Only if using input_form.py
```

---

## 🎯 What Gets Generated

The AI generates a structured learning path with:

1. **Overview** - 2-3 sentence summary
2. **Milestones** - Key achievement points
3. **Curriculum** - Day-by-day breakdown with:
   - Topic for each day
   - Learning objectives (actionable tasks)
   - Estimated hours
   - Real URLs to resources (videos, articles, docs)
   - Due dates (if start_date provided)

**Features:**
- ✅ Real, working URLs (no placeholders)
- ✅ Content tailored to time budget
- ✅ Progression: Foundation → Application → Integration → Mastery
- ✅ Actionable objectives (not vague)

---

## 📚 Additional Documentation

- **[REACT_INTEGRATION.md](REACT_INTEGRATION.md)** - Complete React/TypeScript integration guide with components
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Component structure and data flow (optional)
- **[example_usage.py](example_usage.py)** - Python code examples

---

## 🐛 Troubleshooting

**"API key not found"**
- Set `ANTHROPIC_API_KEY` environment variable

**"anthropic package not installed"**
```bash
pip install anthropic
```

**CORS errors in React**
- Make sure `api_server.py` is running
- Check `allow_origins` in `api_server.py` includes your frontend URL

**JSON parsing errors**
- Check API key is valid
- Verify internet connection
- Try again (API might be temporarily unavailable)

---

## 🔄 Migration Notes

This is a simplified, standalone version. Key differences from original app:
- ✅ No template system (direct topic input)
- ✅ No database storage (returns dict directly)
- ✅ Focused on learning paths only
- ✅ Simplified API (easier to integrate)

The core AI prompt logic is identical to the original app, ensuring the same quality.

---

## 📝 For AI Readers

**If you're an AI reading this codebase:**

1. **Start with this README.md** - Complete overview
2. **Check REACT_INTEGRATION.md** - If integrating with React
3. **Review example_usage.py** - See how everything works
4. **Read ARCHITECTURE.md** - If you need to understand component structure

**Key Files:**
- `generator.py` - Main entry point for learning paths
- `ai_chat.py` - AI chat assistant
- `api_server.py` - FastAPI backend for React apps
- `ai_prompts.py` - Prompt templates
- `scheduler.py` - Date scheduling logic
