# 🎓 LearnPath AI

An AI-powered learning path planner and progress tracker that helps you structure your learning journey with personalized curriculum generation, milestone tracking, and intelligent resource recommendations.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![Anthropic](https://img.shields.io/badge/Claude-API-orange.svg)

## 🌟 Features

### Day 1 - Core Features (Current)
- **🚀 AI Learning Path Generator**
  - Input your learning goal and timeframe
  - Claude AI generates a complete day-by-day curriculum
  - Structured breakdown with topics, subtopics, and time estimates
  - Curated learning resources for each topic
  - Visual timeline and roadmap view

- **📊 Progress Tracker**
  - Check off topics as you complete them
  - Visual progress bar showing completion percentage
  - Track time spent on each topic
  - Learning streak counter
  - Detailed progress statistics

- **💾 Database Storage**
  - Save multiple learning paths
  - Persistent progress tracking
  - View and manage all your learning journeys

### Coming Soon (Roadmap)

**Day 2 - Enhanced Features**
- AI Learning Assistant with built-in chat
- Contextual help based on current topic
- Practice problem generator
- Adaptive learning recommendations

**Day 3 - Analytics & Resources**
- Learning analytics dashboard
- Time tracking per topic
- Learning velocity metrics
- Knowledge gap identification
- Advanced resource library

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))

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

3. **Set up your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env and add your Anthropic API key
   # ANTHROPIC_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   - Open your browser to `http://localhost:8501`
   - Start creating your learning path!

## 📖 Usage Guide

### Creating Your First Learning Path

1. **Enter Your Goal**
   - Be specific about what you want to learn
   - Examples: "Learn Python programming", "Master Machine Learning", "Become a Web Developer"

2. **Set Your Timeframe**
   - Choose how many days you want to dedicate (1-365 days)
   - The AI will create a day-by-day plan that fits your schedule

3. **Generate Path**
   - Click "Generate Learning Path"
   - Wait for Claude AI to create your personalized curriculum
   - Review the generated plan with topics, subtopics, and resources

4. **Track Progress**
   - Check off topics as you complete them
   - Monitor your progress with visual indicators
   - Track your learning streak

### Managing Multiple Paths

- View all your learning paths in the sidebar
- Switch between different learning journeys
- Track progress across multiple goals simultaneously

## 🏗️ Project Structure

```
AI-Learning-Project/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── ai_helpers.py      # Claude API integration
│   ├── path_generator.py  # Learning path logic
│   └── database.py        # SQLite operations
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI**: Claude API (Anthropic)
- **Database**: SQLite
- **Language**: Python 3.8+

## 💡 How It Works

1. **User Input**: You provide a learning goal and timeframe
2. **AI Generation**: Claude AI analyzes your goal and creates a structured curriculum
3. **Database Storage**: The learning path is saved to SQLite for persistence
4. **Progress Tracking**: As you learn, mark topics complete and track your progress
5. **Visualization**: See your progress through intuitive charts and progress bars

## 🎯 Example Learning Goals

Try these examples to get started:

- "Learn Python in 14 days"
- "Master React.js in 30 days"
- "Understand Machine Learning fundamentals in 21 days"
- "Become proficient in SQL in 10 days"
- "Learn Data Science with Python in 60 days"

## 📊 Database Schema

The application uses SQLite with three main tables:

- **learning_paths**: Stores learning goals and metadata
- **topics**: Stores curriculum breakdown with topics and resources
- **progress_log**: Tracks completion and time spent

## 🔐 API Key Setup

### Getting Your Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

### Environment Variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

**Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

## 🚀 Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Add your `ANTHROPIC_API_KEY` in the Secrets section
5. Deploy!

### Local Production

```bash
# Install dependencies
pip install -r requirements.txt

# Run with production settings
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## 🤝 Contributing

Contributions are welcome! Here are some areas where you can help:

- Add new features from the roadmap
- Improve UI/UX
- Add more AI capabilities
- Enhance analytics
- Write tests
- Improve documentation

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Claude AI](https://www.anthropic.com/claude)
- Inspired by modern learning platforms

## 📧 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section below
2. Open an issue on GitHub
3. Review the documentation

## 🐛 Troubleshooting

### API Key Issues
- Ensure your API key is correctly set in `.env`
- Verify the key is valid in the Anthropic Console
- Restart the application after updating `.env`

### Database Issues
- Delete `learnpath.db` to reset the database
- Check file permissions in the project directory

### Installation Issues
- Ensure Python 3.8+ is installed
- Try creating a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

## 🎓 Learning Tips

- **Be Consistent**: Try to complete at least one topic per day
- **Take Notes**: Keep a learning journal alongside the tracker
- **Practice**: Don't just read - implement what you learn
- **Review**: Regularly review completed topics to reinforce learning
- **Ask Questions**: Use the resources provided for each topic

## 🔮 Future Enhancements

- Spaced repetition system
- Quiz generation
- Certificate generation
- Social features (share paths)
- Mobile app
- Integration with YouTube, Coursera, etc.
- Gamification elements
- Collaborative learning paths

---

**Made with ❤️ for learners everywhere**

Happy Learning! 🚀
