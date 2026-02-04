"""
FastAPI Backend Server for React/TypeScript Frontend

This creates a REST API that wraps the learning path generator and AI chat,
making it easy to integrate with React, Vue, or any frontend framework.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os

# Import our generator and chat modules
from generator import LearningPathGenerator
from ai_chat import AIChatAssistant

app = FastAPI(
    title="Learning Path Generator API",
    description="API for generating learning paths and AI chat assistance",
    version="1.0.0"
)

# Enable CORS for frontend
# Update allow_origins with your frontend URL in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default
        "http://localhost:3000",  # Create React App default
        "http://localhost:5174",  # Vite alternate
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize generators (will use environment variables for API keys)
try:
    generator = LearningPathGenerator()
    chat_assistant = AIChatAssistant()
except ValueError as e:
    print(f"Warning: {e}")
    print("Make sure ANTHROPIC_API_KEY is set in environment variables")
    generator = None
    chat_assistant = None


# ============================================================================
# Request/Response Models
# ============================================================================

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


class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[dict]] = None


class ChatResponse(BaseModel):
    response: str


class SuggestLearningRequest(BaseModel):
    goal: str
    current_skills: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    message: str


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint"""
    return {
        "status": "ok",
        "message": "Learning Path Generator API is running"
    }


@app.get("/api/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    if generator is None or chat_assistant is None:
        return {
            "status": "error",
            "message": "API keys not configured"
        }
    return {
        "status": "ok",
        "message": "API is healthy"
    }


@app.post("/api/generate-path")
async def generate_learning_path(request: LearningPathRequest):
    """
    Generate a learning path for a given topic
    
    Example request:
    {
        "topic": "prompt engineering",
        "timeframe": 30,
        "hours_per_day": 2.0,
        "skip_weekends": true
    }
    """
    if generator is None:
        raise HTTPException(
            status_code=503,
            detail="Learning path generator not initialized. Check API key configuration."
        )
    
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


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat with AI assistant
    
    Example request:
    {
        "message": "What should I learn to become an AI engineer?",
        "conversation_history": []  // Optional
    }
    """
    if chat_assistant is None:
        raise HTTPException(
            status_code=503,
            detail="AI chat assistant not initialized. Check API key configuration."
        )
    
    try:
        response = chat_assistant.chat(
            request.message,
            conversation_history=request.conversation_history
        )
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/suggest-learning", response_model=ChatResponse)
async def suggest_learning_path(request: SuggestLearningRequest):
    """
    Get AI suggestions for learning path
    
    Example request:
    {
        "goal": "become an AI engineer",
        "current_skills": "I know Python basics"  // Optional
    }
    """
    if chat_assistant is None:
        raise HTTPException(
            status_code=503,
            detail="AI chat assistant not initialized. Check API key configuration."
        )
    
    try:
        response = chat_assistant.suggest_learning_path(
            request.goal,
            current_skills=request.current_skills
        )
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/compare-topics", response_model=ChatResponse)
async def compare_topics(
    topic1: str,
    topic2: str,
    context: Optional[str] = None
):
    """
    Compare two learning topics
    
    Query parameters:
    - topic1: First topic to compare
    - topic2: Second topic to compare
    - context: Optional context (e.g., "I want to work in data science")
    """
    if chat_assistant is None:
        raise HTTPException(
            status_code=503,
            detail="AI chat assistant not initialized. Check API key configuration."
        )
    
    try:
        response = chat_assistant.compare_topics(topic1, topic2, context)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Run Server
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("Learning Path Generator API Server")
    print("=" * 60)
    print("\nStarting server on http://localhost:8000")
    print("API docs available at http://localhost:8000/docs")
    print("\nMake sure ANTHROPIC_API_KEY is set in environment variables")
    print("=" * 60)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on code changes
    )

