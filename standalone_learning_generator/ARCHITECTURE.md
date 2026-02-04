# Architecture Overview

## 📊 Component Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    User Input (Frontend)                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  input_form.py (Streamlit)                           │   │
│  │  - Topic input                                        │   │
│  │  - Timeframe, hours per day                          │   │
│  │  - Scheduling options (weekends, weekdays, dates)    │   │
│  │  - Proficiency level                                 │   │
│  │  - Focus areas (optional)                            │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              LearningPathGenerator (generator.py)            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  1. Receives user input                              │   │
│  │  2. Calls ai_prompts.py to build prompts            │   │
│  │  3. Sends to Claude AI                               │   │
│  │  4. Parses JSON response                             │   │
│  │  5. Calls scheduler.py to add calendar dates        │   │
│  │  6. Returns complete learning path                   │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌──────────────────┐          ┌──────────────────┐
│  ai_prompts.py   │          │   scheduler.py   │
│                  │          │                  │
│  - Builds system │          │  - Parses dates  │
│    prompt        │          │  - Calculates    │
│  - Builds user   │          │    due dates     │
│    prompt        │          │  - Handles       │
│  - Includes      │          │    constraints   │
│    JSON schema   │          │  - Skips         │
│                  │          │    unavailable   │
│                  │          │    days          │
└──────────────────┘          └──────────────────┘
        │                               │
        └───────────────┬───────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    Generated Learning Path                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  {                                                    │   │
│  │    "overview": "...",                                │   │
│  │    "milestones": [...],                              │   │
│  │    "curriculum": [                                   │   │
│  │      {                                               │   │
│  │        "day": 1,                                     │   │
│  │        "topic": "...",                               │   │
│  │        "learning_objectives": [...],                 │   │
│  │        "estimated_hours": 2.0,                       │   │
│  │        "due_date": "2025-01-01",  // if scheduled   │   │
│  │        "resources": [...]                            │   │
│  │      }                                               │   │
│  │    ],                                                │   │
│  │    "metadata": {...}                                 │   │
│  │  }                                                   │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## 🔑 Key Components

### 1. **generator.py** - Main Orchestrator
- Initializes Anthropic API client
- Coordinates between prompts and scheduler
- Handles API calls and JSON parsing
- Returns structured learning path

### 2. **ai_prompts.py** - Prompt Engineering
- Builds system prompts with requirements
- Creates user prompts with topic and constraints
- Includes JSON schema for structured output
- Adapts to proficiency level and focus areas

### 3. **scheduler.py** - Date Management
- Parses unavailable dates from strings
- Calculates due dates based on constraints
- Handles weekend/weekday skipping
- Manages date ranges and formatting

### 4. **input_form.py** - User Interface
- Streamlit form components
- Collects all user inputs
- Provides scheduling presets
- Validates input before submission

## 🔄 Data Flow

1. **User Input** → Form collects: topic, timeframe, hours, schedule preferences
2. **Prompt Generation** → ai_prompts.py builds detailed prompts
3. **AI Generation** → Claude API generates structured JSON curriculum
4. **Date Scheduling** → scheduler.py adds calendar dates respecting constraints
5. **Output** → Complete learning path with dates, resources, objectives

## 🎯 Scheduling Logic

The scheduler respects multiple constraints in priority order:

1. **Specific unavailable dates** (highest priority)
   - Parsed from strings like "Nov 20-22, Dec 1"
   
2. **Skip weekends flag**
   - If True, skips Saturday (5) and Sunday (6)
   
3. **Skip specific weekdays**
   - List of weekday numbers to skip
   - Example: [2, 3, 4] skips Wed, Thu, Fri
   
4. **Available days**
   - Days that pass all checks get scheduled

## 📝 Prompt Structure

The AI prompt includes:

- **System Prompt**: Instructions, requirements, JSON schema
- **User Prompt**: Topic, timeframe, constraints, quality checklist
- **Adaptive Content**: Adjusts based on hours_per_day and proficiency
- **Focus Areas**: Prioritizes specific topics if provided
- **Additional Requests**: Incorporates user preferences

## 🚀 Integration Points

### For Python Apps:
```python
from generator import LearningPathGenerator
generator = LearningPathGenerator(api_key="...")
path = generator.generate_learning_path(...)
```

### For Streamlit Apps:
```python
from input_form import render_learning_input_form
form_data = render_learning_input_form()
```

### For Other Frameworks:
- Extract logic from `input_form.py`
- Adapt to your UI framework (Flask, FastAPI, React, etc.)
- Use `generator.py` directly for backend logic

## 🔧 Customization Points

1. **Prompt Customization**: Edit `ai_prompts.py` to change:
   - Content depth requirements
   - Resource types
   - Learning style emphasis
   - Difficulty progression

2. **Scheduling Rules**: Edit `scheduler.py` to add:
   - Custom availability patterns
   - Time-of-day constraints
   - Recurring events

3. **Input Fields**: Edit `input_form.py` to add:
   - Learning style preferences
   - Tool/technology filters
   - Certification goals
   - Budget constraints

