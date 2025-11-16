# 🎯 GoalPath AI

An AI-powered universal goal planning platform that helps you achieve any goal - from learning new skills to career transitions, freelancing success, project completion, and personal achievements.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![Multi--Model](https://img.shields.io/badge/AI-Multi--Model-orange.svg)

## 🌟 What Makes GoalPath AI Special

GoalPath AI is not just another to-do list or learning platform. It's a complete goal achievement system powered by multiple AI models that understands **5 different types of goals** and provides specialized guidance for each:

- 📚 **Learning & Skills** - Master new subjects with structured curricula
- 💼 **Career Transition** - Land your dream job with targeted action plans
- 💰 **Freelance & Business** - Build your income streams strategically
- 🚀 **Project Completion** - Ship your projects from idea to launch
- 🎯 **Personal Achievement** - Reach personal milestones with proven strategies

## ✨ Key Features

### 💬 General AI Chat - Ask Anything (NEW in v1.4.0!)
- **Available from Home Screen** - Chat with AI immediately upon opening the app
- **Pre-Decision Advice** - Get guidance BEFORE creating a goal plan
- **12 AI Models** - Choose from Claude, OpenAI, Gemini, DeepSeek, Mistral, Qwen
- **Voice-Enabled** - Use voice input/output for natural conversations
- **Career Guidance** - Ask about learning paths, job opportunities, skill difficulty
- **Full Conversation** - Multi-turn chat with context awareness
- **Example Questions:** "What should I learn to become an AI engineer?", "Is supervised learning harder than reinforcement learning?"

### ⏱️ Time Tracking & AI Coaching
- **Smart Timer** - Start/stop timer with HH:MM:SS display for focused work sessions
- **Manual Time Entry** - Add time manually when you forget to track
- **Actual vs Estimated** - See variance between planned and actual time spent
- **AI Progress Review** - Get performance analysis, insights, and actionable recommendations
- **Conversational AI Coach** - Chat naturally with your AI coach about your goals
- **Voice-Enabled Chat** - Use voice input/output for hands-free coaching conversations

### 📋 50+ Goal Templates
- **Quick-Start** - Choose from 50+ pre-made templates across all goal types
- **Fully Customizable** - Templates are smart defaults, all fields remain editable
- **Smart Search** - Find templates by keywords, tags, or goal type
- **Proven Structures** - Realistic timeframes and hours/day based on real achievements
- **Special Tags** - Remote-Friendly, Income-Generating, Beginner-Friendly, Portfolio-Building, etc.

### 🌟 Universal Goal Planning
- **5 Goal Types** with specialized AI coaching for each
- **Type-Specific Prompts** - Career goals get job search tactics, freelance goals get client acquisition strategies, etc.
- **Priority System** - AI assigns high/medium/low priorities (🔴🟡🟢) to keep you focused
- **Progress Tracking** - Know if you're on track with expected vs. actual progress

### 📅 Date-Aware Smart Scheduling
- **Calendar Dates** - See actual due dates (e.g., "📅 Nov 16, 2025") instead of abstract "Day 1, Day 2"
- **Flexible Time Planning** - Set hours per day (default 2 hours), easily customizable
- **Unavailable Dates** - Mark specific dates or recurring days you can't work
- **Automatic Rescheduling** - Adjust remaining tasks without losing completed progress
- **Color-Coded Status** - 🔴 Overdue, 🟡 Due Today, ✅ Completed, ⚪ Upcoming

### 🤖 Multi-Model AI Tutor
- **15+ AI Models** across 6 providers (Claude, OpenAI, Google Gemini, DeepSeek, Mistral, Qwen)
- **Vision Capabilities** - Upload homework, diagrams, screenshots for instant analysis
- **Model Switching** - Compare responses from different AI models
- **Chat History** - Persistent conversations per goal plan

### 📎 File Upload & Analysis
- **Images** - Solve problems, explain diagrams, OCR handwritten notes
- **PDFs** - Extract text, answer questions, summarize
- **Documents** - Analyze Word docs, text files
- **YouTube Auto-Embed** - Watch tutorial videos inline without leaving the app

### 📊 Smart Progress Tracking
- **On-Track Indicator** - See if you're ahead or behind schedule (✅⚠️)
- **Visual Progress** - Completion percentage, streak counters
- **Status Management** - Active, On Hold, Archived, Deleted
- **Activity Metrics** - Time spent, completed topics, active days
- **Resource Links** - Add links to your own study materials (Google Drive, Notion, local files) (NEW!)

### 📄 Export & Share
- **Calendar Export (.ics)** - Import your goal plan into Google Calendar, Outlook, Apple Calendar, or any calendar app (NEW!)
- **PDF Export** - Download goal plans for offline use or sharing with mentors/coaches
- **Mobile Optimized** - Works perfectly on phones and tablets
- **Password Protected** - Secure your data with persistent cookie-based authentication

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- At least ONE AI provider API key (Claude recommended)
- A strong password for securing your instance

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Learning-Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env and add your credentials
   nano .env  # or use your preferred editor
   ```

4. **Configure .env file**
   ```env
   # REQUIRED: Set a strong password
   APP_PASSWORD=your_secure_password_here

   # Add at least ONE AI provider API key
   ANTHROPIC_API_KEY=your_claude_key_here
   # OPENAI_API_KEY=your_openai_key_here
   # DEEPSEEK_API_KEY=your_deepseek_key_here
   # GOOGLE_API_KEY=your_gemini_key_here
   # MISTRAL_API_KEY=your_mistral_key_here
   # QWEN_API_KEY=your_qwen_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the app**
   - Open your browser to `http://localhost:8501`
   - Enter your password (set in APP_PASSWORD)
   - Start planning your goals!

## 🔐 Security & Authentication

### Password Protection

GoalPath AI uses **cookie-based password protection** with 24-hour persistent sessions:

- **Local Development**: Set `APP_PASSWORD` in your `.env` file
- **Streamlit Cloud**: Set `APP_PASSWORD` in Secrets (see deployment section below)
- **Session Duration**: 24 hours (stays logged in even after closing browser)
- **Logout**: Use the 🚪 Logout button in the sidebar

### Changing Your Password

**Local:**
1. Update `APP_PASSWORD` in your `.env` file
2. Restart the app
3. All users will need to login again with the new password

**Streamlit Cloud:**
1. Go to your app settings on Streamlit Cloud
2. Navigate to Secrets section
3. Update `APP_PASSWORD` value
4. Save (app will automatically restart)

### Security Best Practices

- ✅ Use a strong, unique password
- ✅ Never commit `.env` file to git (already in `.gitignore`)
- ✅ Don't share your password publicly
- ✅ Rotate password periodically for production deployments
- ✅ Use different passwords for development and production

## 🎯 Usage Guide

### Using Goal Templates (Quick Start!)

**NEW:** GoalPath AI now includes 50+ pre-made templates to quick-start your goals!

1. **Click "📋 Choose Template" tab**
2. **Browse or search** for templates:
   - Search by keywords (e.g., "remote jobs", "AI", "freelance", "fitness")
   - Filter by goal type (Learning, Career, Freelance, Project, Personal)
3. **Click "Use This Template"** on any template
4. **Customize all fields** - goal text, timeframe, hours/day all editable!
5. **Generate** - AI creates personalized plan based on your customizations

**Popular Templates:**
- 💼 Land Remote AI Engineering Role (International)
- 💰 First 5 Fiverr Clients in 30 Days
- 📚 Master Prompt Engineering
- 🚀 Build & Launch Developer Portfolio Website
- 🎯 Run Your First 5K Race

**All templates include:**
- Proven goal structure
- Realistic timeframes
- Suggested hours/day
- Difficulty level
- Smart tags (Remote-Friendly, Income-Generating, etc.)

**Remember:** Templates are starting points - every field is fully customizable!

### Creating Your First Goal Plan (From Scratch)

1. **Select Goal Type**
   - Choose from: Learning & Skills, Career Transition, Freelance & Business, Project Completion, or Personal Achievement

2. **Enter Your Goal**
   - Examples:
     - 📚 "Learn Prompt Engineering"
     - 💼 "Get hired as AI engineer"
     - 💰 "Get 5 Fiverr clients"
     - 🚀 "Build portfolio website"
     - 🎯 "Run a 10K race"

3. **Set Your Timeframe**
   - Choose 1-365 days based on your goal complexity

4. **Schedule Your Goal (NEW!)**
   - **Start Date**: When you want to begin (default: today)
   - **Hours per Day**: How much time you can dedicate (default: 2 hours)
   - **Advanced Scheduling (Optional)**:
     - Mark unavailable dates (e.g., "Nov 20-22, Dec 1")
     - Skip specific weekdays (Wednesdays, Thursdays, weekends)
     - System automatically adjusts calendar dates around your availability

5. **Generate Goal Plan**
   - AI creates type-specific action plan with calendar dates
   - Review priorities, milestones, and resources
   - See actual due dates (📅 Nov 16, 2025) for each task
   - Plan is automatically saved

6. **Execute & Track**
   - Check off tasks as you complete them
   - See color-coded status: 🔴 Overdue, 🟡 Due Today, ⚪ Upcoming
   - Monitor your on-track status
   - Use **Reschedule Plan** if you need to adjust dates
   - Use AI Tutor for questions
   - Export to PDF when needed

### Using the AI Tutor

1. Open any goal plan
2. Click the "🤖 AI Tutor" tab
3. Select your preferred AI model
4. Ask questions or upload files for analysis
5. Switch models to compare responses

### Uploading Files

- Click "Upload Image or File"
- Supported: PNG, JPG, PDF, TXT, DOCX
- Add your question
- AI analyzes and responds based on file content

### Adding Your Own Resource Links (NEW!)

**Keep your study materials organized:**

1. Expand any task in your goal plan
2. Scroll to "📎 My Resource Links" section
3. Add links to your external resources (one per line):
   - Google Drive folders
   - Notion pages
   - Saved PDF files
   - YouTube playlists
   - GitHub repos
   - Any other study materials

**Examples:**
```
https://drive.google.com/folder/my-python-notes
https://notion.so/my-study-guide
~/Documents/python-tutorial.pdf
https://github.com/myusername/learning-project
```

**Features:**
- Auto-saves as you type
- Web links become clickable (open in new tab)
- Local file paths displayed for reference
- Perfect for quick access to frequently used materials
- Mobile-friendly - tap to open links on the go

### Time Tracking & Coaching (NEW!)

**Tracking Your Time:**
1. Open any goal plan and go to the "📚 Curriculum" tab
2. Expand any task to see time tracking options
3. **Using the Timer:**
   - Click "▶️ Start Timer" to begin tracking
   - Timer shows elapsed time in HH:MM:SS format
   - Click "⏸️ Stop & Save" when done
   - Multiple sessions are tracked automatically
4. **Manual Time Entry:**
   - Enter hours spent (e.g., 2.5 hours)
   - Click "Add Time" to record
   - Perfect for when you forgot to start the timer
5. **View Actual vs Estimated:**
   - See estimated hours vs actual hours spent
   - Green = under estimate, red = over estimate
   - Track variance to improve future planning

**Getting AI Coaching:**
1. Go to "🧠 AI Coach" tab in any goal plan
2. View your progress metrics and time stats
3. Click "📊 Get Progress Review & Coaching" button
4. AI analyzes your:
   - Tasks completed vs total
   - Actual time vs estimated time
   - Days elapsed and pace
   - Patterns and trends
5. Review the coaching report with:
   - Performance Summary
   - Key Insights
   - Actionable Recommendations
6. Past reviews are saved and accessible in the accordion

**Conversational AI Coach:**
1. Go to "💬 AI Coach Chat" tab
2. Chat naturally with your AI coach about your goals
3. Ask questions like:
   - "How am I doing?"
   - "I'm feeling overwhelmed, what should I focus on?"
   - "Should I adjust my timeline?"
4. Use voice input (🎤) for hands-free conversation
5. AI responds with context about YOUR specific goal and data
6. Chat history is saved per goal plan
7. Use quick prompts for common questions

### Rescheduling Your Plan (NEW!)

1. Open any goal plan with calendar dates
2. Expand "📅 Reschedule Plan" section
3. Set new start date for remaining (incomplete) topics
4. Adjust hours per day if needed
5. Optionally update unavailable dates
6. Click "Reschedule Incomplete Topics"
7. Completed tasks keep their original dates - only incomplete tasks are rescheduled

**Why Reschedule?**
- Life happens - vacations, emergencies, schedule changes
- Adjust your time commitment up or down
- Get back on track after falling behind
- Completed work is never lost or changed

### Exporting to PDF

1. Open a goal plan
2. Expand "⚙️ Advanced Options"
3. Click "📥 Download as PDF"
4. Click "💾 Save PDF"
5. File downloads as `goalpath_[your_goal].pdf` (now includes calendar dates!)

### Exporting to Calendar (.ics) (NEW!)

**Take your goal plan to your daily calendar!**

1. Open any goal plan with calendar dates
2. Expand "⚙️ Advanced Options"
3. Click "📅 Export to Calendar (.ics)"
4. Click "💾 Download Calendar File"
5. File downloads as `goalpath_[your_goal]_[date].ics`

**Import into your calendar app:**

- **Google Calendar:**
  - Go to Settings → Import & Export → Import
  - Select the downloaded .ics file

- **Microsoft Outlook:**
  - File → Open & Export → Import/Export
  - Select "Import an iCalendar (.ics) file"

- **Apple Calendar:**
  - File → Import → Select .ics file
  - Or simply double-click the .ics file

- **Other calendar apps:**
  - Look for Import, Add Calendar, or Subscribe option

**What gets imported:**
- Each task as a calendar event on its due date
- Event duration based on estimated hours
- Full task details including subtopics and resources
- Priority level in event description
- Completed tasks marked as done
- All events categorized by your goal type

**Benefits:**
- See your goal plan in your daily calendar view
- Get calendar notifications for upcoming tasks
- Integrate goal tracking with your existing workflow
- Sync across all your devices automatically
- Perfect for time blocking and scheduling

## 📁 Project Structure

```
AI-Learning-Project/
├── app.py                    # Main Streamlit application
├── utils/
│   ├── auth.py              # Password authentication system
│   ├── ai_helpers.py        # Claude API integration
│   ├── ai_providers.py      # Multi-model AI system
│   ├── path_generator.py   # Goal planning logic
│   ├── database.py          # SQLite operations (with time tracking & coaching)
│   ├── date_scheduler.py    # Calendar date scheduling utilities
│   ├── templates.py         # 50+ goal templates library
│   └── voice_handler.py     # Voice input/output interface
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
├── DEPLOYMENT.md           # Step-by-step deployment guide
├── MOBILE_GUIDE.md         # Mobile optimization documentation
├── FEATURE_SUMMARY.md      # Complete feature documentation
└── README.md               # This file
```

## 🚀 Deployment

**For complete step-by-step deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)**

**Quick Summary:**

### Recommended: Streamlit Cloud (Best for Mobile)

Perfect for your use case - access GoalPath AI from anywhere on your phone!

**Steps:**
1. Get Anthropic API key ([console.anthropic.com](https://console.anthropic.com/))
2. Push code to GitHub
3. Deploy on [share.streamlit.io](https://share.streamlit.io)
4. Add secrets (APP_PASSWORD + API keys)
5. Access from mobile - add to home screen!

**Time:** 15 minutes | **Cost:** FREE (Anthropic has free tier)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed walkthrough with screenshots and mobile setup tips.

---

### Option 1: Streamlit Cloud (Recommended)

1. **Prepare Your Repository**
   ```bash
   # Ensure .env is NOT committed
   git status

   # Commit your changes
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select the repository and branch
   - Set main file path: `app.py`

3. **Configure Secrets**

   In the Streamlit Cloud app settings, go to "Secrets" and add:

   ```toml
   # REQUIRED: Your app password
   APP_PASSWORD = "your_secure_password_here"

   # Add your AI provider API keys
   ANTHROPIC_API_KEY = "your_claude_key"
   OPENAI_API_KEY = "your_openai_key"
   DEEPSEEK_API_KEY = "your_deepseek_key"
   GOOGLE_API_KEY = "your_gemini_key"
   MISTRAL_API_KEY = "your_mistral_key"
   QWEN_API_KEY = "your_qwen_key"

   # Optional: Cookie encryption key (random string)
   COOKIE_SECRET_KEY = "some-random-secret-key-for-cookies"
   ```

4. **Deploy!**
   - Click "Deploy"
   - Wait for deployment to complete
   - Access your app at `https://your-app-name.streamlit.app`

### Option 2: Local Production Server

```bash
# Install dependencies
pip install -r requirements.txt

# Set up .env file with credentials
cp .env.example .env
nano .env  # Add APP_PASSWORD and API keys

# Run with production settings
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### Option 3: Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
# Build and run
docker build -t goalpath-ai .
docker run -p 8501:8501 --env-file .env goalpath-ai
```

## 🔧 Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Providers**: Claude, OpenAI, Google Gemini, DeepSeek, Mistral, Qwen
- **Authentication**: streamlit-cookies-manager with encrypted cookies
- **Database**: SQLite
- **File Processing**: PyPDF2, python-docx, Pillow, pytesseract
- **PDF Generation**: ReportLab
- **Language**: Python 3.8+

## 🔑 Getting API Keys

### Anthropic Claude (Recommended)
1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up and create API key
3. Add to `.env`: `ANTHROPIC_API_KEY=sk-ant-...`

### OpenAI
1. Go to [platform.openai.com](https://platform.openai.com/)
2. Create API key
3. Add to `.env`: `OPENAI_API_KEY=sk-...`

### Google Gemini
1. Go to [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Create API key
3. Add to `.env`: `GOOGLE_API_KEY=...`

### DeepSeek
1. Go to [platform.deepseek.com](https://platform.deepseek.com/)
2. Create API key
3. Add to `.env`: `DEEPSEEK_API_KEY=...`

### Mistral AI
1. Go to [console.mistral.ai](https://console.mistral.ai/)
2. Create API key
3. Add to `.env`: `MISTRAL_API_KEY=...`

### Qwen (Alibaba Cloud)
1. Go to [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com/)
2. Create API key
3. Add to `.env`: `QWEN_API_KEY=...`

## 📱 Mobile Optimization

GoalPath AI is fully optimized for mobile devices:

- ✅ Touch-friendly buttons (44px minimum)
- ✅ Responsive text inputs (16px font prevents zoom)
- ✅ Mobile-optimized spacing and layouts
- ✅ Hamburger sidebar menu
- ✅ Responsive YouTube embeds
- ✅ File upload works on mobile cameras

Test on mobile by visiting your deployed URL from your phone!

## 🐛 Troubleshooting

### Authentication Issues

**Problem**: Can't login / "Incorrect password"
- Check `APP_PASSWORD` in `.env` (local) or Secrets (cloud)
- Ensure no extra spaces in password
- Try resetting cookies: Clear browser data for the site

**Problem**: Logged out too quickly
- Check system time is correct
- Cookie expiration is 24 hours - may need to login daily

### API Key Issues

**Problem**: "API key not configured"
- Ensure API key is in `.env` (local) or Secrets (cloud)
- Restart app after adding keys
- Check for typos in environment variable names

### File Upload Issues

**Problem**: Can't upload images on mobile
- Grant browser camera/file permissions
- Try different browser (Chrome/Safari)
- Check file size (<10MB recommended)

### Deployment Issues

**Problem**: App crashes on Streamlit Cloud
- Check all secrets are properly formatted in TOML
- Ensure `requirements.txt` includes all dependencies
- Check logs in Streamlit Cloud dashboard

**Problem**: Password not working after deployment
- Verify `APP_PASSWORD` is in Secrets (not .env)
- Secrets must use TOML format: `APP_PASSWORD = "value"`
- Redeploy app after changing secrets

## 💡 Best Practices

### For Goal Planning
- Be specific with goals ("Learn Python for data analysis" vs "Learn Python")
- Choose realistic timeframes
- Review AI-assigned priorities - high priority items first
- Check your on-track indicator daily

### For Security
- Use strong passwords (12+ characters, mixed case, numbers, symbols)
- Don't share passwords in screenshots or videos
- Keep API keys secret
- Rotate passwords quarterly for production use

### For Performance
- Configure only the AI providers you need
- Close unused goal plans
- Archive completed goals
- Export to PDF for long-term storage

## 🎯 Example Goals by Type

### 📚 Learning & Skills
- "Master Prompt Engineering in 14 days"
- "Learn Python for Data Science in 30 days"
- "Become proficient in SQL in 21 days"

### 💼 Career Transition
- "Get hired as AI Engineer in 60 days"
- "Land remote software job in 90 days"
- "Transition from marketing to UX design in 120 days"

### 💰 Freelance & Business
- "Get first 5 Fiverr clients in 30 days"
- "Earn $1000/month freelancing in 60 days"
- "Launch SaaS MVP in 90 days"

### 🚀 Project Completion
- "Build and deploy portfolio website in 14 days"
- "Launch mobile app to App Store in 60 days"
- "Complete YouTube course series in 30 days"

### 🎯 Personal Achievement
- "Run a 10K race in 90 days"
- "Learn guitar basics in 60 days"
- "Lose 10 pounds in 45 days"

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Voice interface for hands-free planning
- [ ] Interactive quiz generation
- [ ] Resource rating system
- [ ] Social features (share goal plans)
- [ ] Calendar integration
- [ ] Notification system
- [ ] Dark mode
- [ ] Multi-language support

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by multiple AI providers
- Cookie auth via [streamlit-cookies-manager](https://github.com/ktosiek/streamlit-cookies-manager)
- Inspired by modern productivity and learning platforms

## 📧 Support

For issues, questions, or feature requests:
1. Check this README and troubleshooting section
2. Review the [FEATURE_SUMMARY.md](FEATURE_SUMMARY.md) for detailed feature documentation
3. Open an issue on GitHub

---

**Made with ❤️ for goal achievers everywhere**

Start achieving your goals today! 🚀🎯
