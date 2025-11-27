# smart-study-assistant
# Smart Study Assistant

An AI-powered learning companion that transforms passive learning materials into interactive experiences. This application helps students engage with educational content through AI-driven chat, automatic summarization, quiz generation, and multi-language support.

## 🌟 Features

- **AI Chat Assistant**: Interactive Q&A powered by DeepSeek API to answer questions about your study materials
- **Text Summarization**: Automatically extract key points from lengthy documents using Azure AI Language
- **Quiz Generation**: Create practice questions based on your learning content
- **Text Analysis**: Identify key phrases, entities, and sentiment in educational materials
- **Multi-language Translation**: Break language barriers with Azure AI Translator supporting 100+ languages

## 🛠️ Technology Stack

### Backend
- Python 3.8+
- Flask (Web Framework)
- Requests (HTTP Library)

### AI Services
- **DeepSeek API**: Natural language processing and conversational AI
- **Azure AI Language**: Text analytics, summarization, and key phrase extraction
- **Azure AI Translator**: Multi-language translation capabilities

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)

## 📋 Prerequisites

Before running this application, you need:

1. Python 3.8 or higher installed on your system
2. DeepSeek API access
3. Microsoft Azure subscription with:
   - Azure AI Language resource
   - Azure AI Translator resource

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/wakuwakulala/smart-study-assistant.git
cd smart-study-assistant
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, install these packages manually:
```bash
pip install flask requests python-dotenv
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory of the project:

**On Windows:**
```bash
type nul > .env
```

**On macOS/Linux:**
```bash
touch .env
```

Open the `.env` file with your text editor and add the following configuration:
```env
# DeepSeek API Configuration
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_API_BASE=https://api.deepseek.com

# Azure AI Language Configuration
AZURE_LANGUAGE_KEY=your_azure_language_key_here
AZURE_LANGUAGE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/

# Azure AI Translator Configuration
AZURE_TRANSLATOR_KEY=your_azure_translator_key_here
AZURE_TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com/
AZURE_TRANSLATOR_REGION=your_azure_region_here
```

## 🔑 Obtaining API Keys and Endpoints

### DeepSeek API

1. Visit [DeepSeek Platform](https://platform.deepseek.com/)
2. Sign up for an account or log in if you already have one
3. Navigate to the **API Keys** section in your dashboard
4. Click **"Create New Key"** or **"Generate API Key"**
5. Copy the generated API key
6. Paste it into your `.env` file as the value for `DEEPSEEK_API_KEY`

**Example:**
```env
DEEPSEEK_API_KEY=sk-1a2b3c4d5e6f7g8h9i0j
```

### Azure AI Language

1. Go to [Azure Portal](https://portal.azure.com/)
2. Sign in with your Microsoft account
3. Click **"Create a resource"** in the left sidebar
4. Search for **"Language"** or **"Language Service"**
5. Click **Create** and fill in the required information:
   - **Subscription**: Choose your Azure subscription
   - **Resource Group**: Create new or use existing
   - **Region**: Choose a region close to you (e.g., East US, West Europe)
   - **Name**: Give your resource a unique name (e.g., `my-language-service`)
   - **Pricing Tier**: Select Free (F0) tier for testing or Standard (S) for production
6. Click **Review + Create**, then **Create**
7. Once deployment is complete, click **Go to resource**
8. In the left menu, click **Keys and Endpoint**
9. Copy **KEY 1** (or KEY 2) and paste it as `AZURE_LANGUAGE_KEY` in your `.env` file
10. Copy the **Endpoint** URL and paste it as `AZURE_LANGUAGE_ENDPOINT`

**Example:**
```env
AZURE_LANGUAGE_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
AZURE_LANGUAGE_ENDPOINT=https://my-language-service.cognitiveservices.azure.com/
```

### Azure AI Translator

1. In [Azure Portal](https://portal.azure.com/), click **"Create a resource"**
2. Search for **"Translator"** or **"Translator Text"**
3. Click **Create** and fill in the details:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Same as Language Service or create new
   - **Region**: Choose your region (note this value, you'll need it)
   - **Name**: Unique name for your translator resource
   - **Pricing Tier**: Free (F0) or Standard (S0)
4. Click **Review + Create**, then **Create**
5. Go to the resource after deployment
6. Click **Keys and Endpoint** in the left menu
7. Copy **KEY 1** and paste it as `AZURE_TRANSLATOR_KEY`
8. Copy the **Location/Region** (e.g., "eastus", "westeurope") and paste it as `AZURE_TRANSLATOR_REGION`
9. The endpoint is typically `https://api.cognitive.microsofttranslator.com/`

**Example:**
```env
AZURE_TRANSLATOR_KEY=z9y8x7w6v5u4t3s2r1q0p9o8n7m6l5k4
AZURE_TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com/
AZURE_TRANSLATOR_REGION=eastus
```

## ▶️ Running the Application

### Start the Development Server

Make sure your virtual environment is activated and you're in the project directory:
```bash
python app.py
```

You should see output similar to:
```
 * Running on http://127.0.0.1:5000
 * Running on http://localhost:5000
```

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

To stop the server, press `Ctrl + C` in the terminal.

## 📁 Project Structure
```
smart-study-assistant/
│
├── app.py                     # Main Flask application with API routes
├── .env                       # Environment variables (DO NOT commit to Git)
├── .gitignore                # Files and folders to ignore in Git
├── requirements.txt          # Python package dependencies
├── README.md                 # Project documentation (this file)
│
├── templates/                # HTML templates
│   └── index.html           # Main web interface
│
├── static/                   # Static assets
│   ├── css/                 # Stylesheets
│   │   └── style.css
│   ├── js/                  # JavaScript files
│   │   └── main.js
│   └── images/              # Images and icons
│
└── venv/                     # Virtual environment (not committed)
```

## 📖 Usage Guide

### 1. AI Chat Assistant

**Purpose**: Ask questions and get intelligent answers about your study materials.

**How to use:**
1. Navigate to the **Chat** section
2. Type your question in the input box (e.g., "Explain photosynthesis")
3. Press Enter or click the Send button
4. The AI will provide a detailed response
5. Continue the conversation with follow-up questions

**Tips:**
- Be specific with your questions for better answers
- You can ask for explanations, examples, or clarifications
- The AI maintains context within the conversation

### 2. Text Summarization

**Purpose**: Extract key points from lengthy study materials.

**How to use:**
1. Go to the **Summarize** section
2. Paste your text content (e.g., textbook chapter, article)
3. Optionally select the desired summary length
4. Click **"Generate Summary"**
5. Review the condensed version highlighting main ideas

**Best for:**
- Long articles or research papers
- Textbook chapters
- Lecture notes
- Study guides

### 3. Quiz Generation

**Purpose**: Create practice questions to test your knowledge.

**How to use:**
1. Navigate to the **Quiz** section
2. Input your study content or topic
3. Select quiz parameters:
   - Number of questions
   - Question type (multiple choice, true/false, etc.)
   - Difficulty level
4. Click **"Generate Quiz"**
5. Take the quiz and check your answers

**Features:**
- Automatically generates relevant questions
- Provides correct answers
- Helps identify knowledge gaps

### 4. Text Analysis

**Purpose**: Identify key concepts, entities, and sentiment in your materials.

**How to use:**
1. Go to the **Analyze** section
2. Paste your text
3. Click **"Analyze Text"**
4. View results showing:
   - Key phrases and important terms
   - Named entities (people, places, organizations)
   - Sentiment analysis (positive, neutral, negative)

**Useful for:**
- Understanding main themes
- Identifying important concepts
- Analyzing tone and perspective

### 5. Multi-language Translation

**Purpose**: Translate study materials between languages.

**How to use:**
1. Navigate to the **Translate** section
2. Enter or paste your text
3. Select source language (or choose "Auto-detect")
4. Select target language from dropdown
5. Click **"Translate"**
6. Copy or use the translated text

**Supports:**
- 100+ languages
- Automatic language detection
- Bidirectional translation

## 🔒 Security Best Practices

### Protecting Your API Keys

⚠️ **CRITICAL: Never expose your API keys publicly!**

**DO:**
- ✅ Store all API keys in the `.env` file
- ✅ Add `.env` to your `.gitignore` file
- ✅ Use environment variables in your code
- ✅ Rotate keys regularly (every 90 days recommended)
- ✅ Use different keys for development and production
- ✅ Revoke keys immediately if compromised

**DON'T:**
- ❌ Hardcode API keys in your source code
- ❌ Commit `.env` file to Git
- ❌ Share keys in screenshots or documentation
- ❌ Send keys via email or chat
- ❌ Include keys in error messages or logs

### .gitignore Configuration

Ensure your `.gitignore` file includes:
```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environment
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
```

### If Your Keys Are Compromised

1. **Immediately revoke** the exposed keys in Azure Portal or DeepSeek Platform
2. **Generate new keys** and update your `.env` file
3. **Review access logs** to check for unauthorized usage
4. **Enable alerts** for unusual activity
5. **Consider implementing** rate limiting and authentication

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue 1: "Module not found" Error

**Error message:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Make sure virtual environment is activated
# Then reinstall dependencies
pip install -r requirements.txt
```

#### Issue 2: "API Key Invalid" Error

**Possible causes:**
- Key was copied incorrectly (extra spaces, line breaks)
- Key has expired or been revoked
- Wrong key type for the service

**Solutions:**
1. Open `.env` file and verify keys are correctly formatted
2. Check for extra whitespace before or after keys
3. Regenerate keys in Azure Portal or DeepSeek Platform
4. Ensure you're using KEY 1 or KEY 2 (not the endpoint)

#### Issue 3: "Connection Timeout" to Azure

**Error message:**
```
ConnectionError: Connection timeout
```

**Solutions:**
1. Check your internet connection
2. Verify endpoint URLs are correct (no typos)
3. Ensure Azure resources are active:
   - Go to Azure Portal
   - Check resource status
   - Verify subscription hasn't expired
4. Try pinging the endpoint to test connectivity

#### Issue 4: Port Already in Use

**Error message:**
```
OSError: [Errno 48] Address already in use
```

**Solutions:**

**Option 1 - Use a different port:**
```python
# In app.py, change:
app.run(debug=True, port=5001)
```

**Option 2 - Kill the process using port 5000:**

On macOS/Linux:
```bash
lsof -ti:5000 | xargs kill -9
```

On Windows:
```bash
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

#### Issue 5: ".env file not found" Error

**Solution:**
1. Verify `.env` file exists in project root directory:
```bash
   ls -la  # macOS/Linux
   dir     # Windows
```
2. If missing, create it:
```bash
   touch .env  # macOS/Linux
   type nul > .env  # Windows
```
3. Make sure you're running the app from the correct directory

#### Issue 6: Azure "Resource Not Found"

**Error message:**
```
404 Resource Not Found
```

**Solutions:**
1. Verify your endpoint URL includes the full path
2. Check API version in the request
3. Ensure resource hasn't been deleted in Azure Portal
4. Confirm you're using the correct endpoint for your region

#### Issue 7: DeepSeek API Rate Limit Exceeded

**Error message:**
```
429 Too Many Requests
```

**Solutions:**
1. Check your DeepSeek plan limits
2. Implement rate limiting in your application
3. Add retry logic with exponential backoff
4. Consider upgrading your DeepSeek plan

## 📊 API Rate Limits and Costs

### DeepSeek API
- **Free Tier**: Check current limits on DeepSeek Platform
- **Paid Tiers**: Various options available
- **Rate Limits**: Varies by plan
- **Best Practice**: Cache responses when possible

### Azure AI Language
- **Free Tier (F0)**:
  - 5,000 text records per month
  - Up to 10 requests per second
- **Standard Tier (S)**:
  - Pay per use
  - Higher throughput
- **Costs**: See [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

### Azure AI Translator
- **Free Tier (F0)**:
  - 2 million characters per month
  - Standard translation only
- **Standard Tier (S0)**:
  - Pay per character
  - Document translation available
- **Costs**: Approximately $10 per million characters

### Cost Management Tips
1. Use free tiers for development and testing
2. Monitor usage in Azure Portal
3. Set up billing alerts
4. Implement caching to reduce API calls
5. Optimize requests (batch processing when possible)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit bug fixes
- ✨ Add new features

### Contribution Process
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Include docstrings for functions and classes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ Liability and warranty not provided

## 🙏 Acknowledgments

- **DeepSeek** for providing powerful conversational AI capabilities
- **Microsoft Azure** for comprehensive AI Language and Translator services
- **Flask** framework for elegant web application development
- **Python Community** for excellent libraries and tools

## 📞 Support and Contact

### Getting Help
- 📖 Check this README first
- 🐛 Search existing [GitHub Issues](https://github.com/wakuwakulala/smart-study-assistant/issues)
- 💬 Open a new issue if your problem isn't addressed

### Reporting Issues
When reporting bugs, please include:
1. Description of the problem
2. Steps to reproduce
3. Expected vs actual behavior
4. Error messages (if any)
5. Your environment:
   - Operating System
   - Python version
   - Browser (if frontend issue)

### Feature Requests
We'd love to hear your ideas! When suggesting features:
1. Describe the feature clearly
2. Explain the use case
3. Provide examples if possible

## 🗺️ Roadmap

### Planned Features
- [ ] User authentication and personal accounts
- [ ] Save and organize study sessions
- [ ] Progress tracking and analytics
- [ ] Flashcard generation
- [ ] Integration with popular note-taking apps
- [ ] Mobile application (iOS/Android)
- [ ] Collaborative study features
- [ ] Voice input and output
- [ ] PDF and document upload support
- [ ] Spaced repetition system

### Recent Updates
- ✅ Initial release with core features
- ✅ Integration with DeepSeek API
- ✅ Azure AI Language support
- ✅ Azure AI Translator integration
- ✅ Basic web interface

## 📚 Additional Resources

### Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [DeepSeek API Docs](https://platform.deepseek.com/docs)
- [Azure AI Language Docs](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure AI Translator Docs](https://learn.microsoft.com/azure/ai-services/translator/)

### Tutorials
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [REST API Best Practices](https://restfulapi.net/)
- [Git and GitHub Tutorial](https://docs.github.com/en/get-started)

---

## ⚡ Quick Start Summary

For experienced developers, here's the TL;DR:
```bash
# Clone and setup
git clone https://github.com/wakuwakulala/smart-study-assistant.git
cd smart-study-assistant
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Configure environment
cp .env.example .env  # Create .env from template
# Edit .env with your API keys

# Run
python app.py
# Visit http://localhost:5000
```

---

**Made with ❤️ for learners everywhere**

*Last updated: November 2024*
