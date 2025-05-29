# 🧠 Task Allocation AI Agent

This is a lightweight AI agent built using [Pydantic AI](https://github.com/astral-sh/pydantic-ai) that converts natural language instructions into structured task data.

## 🔧 Tech Stack

- 🧠 **TogetherAI API** with `Mixtral-8x7B-Instruct` model for language understanding
- ✅ **Pydantic AI** for intelligent agent orchestration
- 🔥 **Logfire** for intelligent logging and monitoring
- 🐍 **Python** with modern dependency management

---

## 🚀 What it does

Transform messy, natural language instructions into clean, structured task data.

### Input Example:
```
"Riya and Aman should finalize the event poster and send it to Anuj by Friday. Priority high."
```

### Output Example:
```json
{
  "tasks": [
    {
      "task_description": "finalize event poster",
      "assignee": "Riya, Aman",
      "deadline": null,
      "priority": "high",
      "status": null
    },
    {
      "task_description": "send poster to Anuj",
      "assignee": "Riya, Aman",
      "deadline": "Friday",
      "priority": "high",
      "status": null
    }
  ]
}
```

### More Examples:

**Input:** `"Sandeep should update the sponsor spreadsheet and set status to In Progress."`

**Output:**
```json
{
  "tasks": [
    {
      "task_description": "update sponsor spreadsheet",
      "assignee": "Sandeep",
      "deadline": null,
      "priority": null,
      "status": "In Progress"
    }
  ]
}
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- TogetherAI API Key
- Logfire API Key

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd task-allocation-agent
```

### 2. Install dependencies
```bash
uv venv
uv sync
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
TOGETHERAI_API_KEY=your_togetherai_api_key_here
LOGFIRE_TOKEN=your_logfire_token_here
```

### 4. Get your TogetherAI API Key
1. Sign up at [Together.ai](https://www.together.ai/)
2. Generate an API key
3. Add it to your `.env` file

### 5. Get your Logfire API Key
1. Sign up at [LogFire](https://pydantic.dev/logfire)
2. Generate an API key
3. Add it to your `.env` file

---

## 🧪 Usage

### Basic Usage
```bash
python my_agent.py
```

### Programmatic Usage
```python
from agent import task_allocation_agent

result = task_allocation_agent(
    user_prompt="John and Sarah should prepare the presentation by tomorrow, high priority",
    model_name="mistralai/mixtral-8x7b-instruct"
)

print(result)
```

### Supported Models
- `openchat/openchat-3.5`
- `mistralai/mistral-7b-instruct`
- `mistralai/mixtral-8x7b-instruct` (recommended)

---

## 📂 Project Structure

```
task-allocation-agent/
├── agent.py              # Main agent logic and model setup
├── my_agent.py           # Example usage script
├── prompt.py             # System prompt and examples
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

---

## 🎯 Features

### Smart Task Parsing
- **Multiple Tasks**: Automatically splits compound instructions
- **Multiple Assignees**: Handles comma-separated assignee lists
- **Natural Deadlines**: Understands "tomorrow", "next Monday", "end of quarter"
- **Priority Detection**: Extracts priority levels (low, medium, high, critical)
- **Status Tracking**: Recognizes status updates (To Do, In Progress, Completed)

### Edge Cases Handled
- Group assignments ("Everyone", "All", "Team")
- Compound tasks with different assignees  
- Implied deadlines and priorities
- Incomplete information (sets to `null`)

---

## 🔍 Monitoring

The agent includes built-in Logfire integration for:
- Request/response logging
- Performance monitoring  
- Error tracking
- Usage analytics

Check your logs at: [Logfire Dashboard](https://logfire-us.pydantic.dev/)

---

## 🧠 How it Works

1. **Input Processing**: Takes natural language task instructions
2. **LLM Analysis**: Uses Mixtral-8x7B to understand context and extract entities
3. **Structured Output**: Returns JSON with standardized task objects
4. **Validation**: Pydantic ensures data consistency and type safety

---

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🧠 Credits

Built by [@Ak62007](https://github.com/Ak62007) using:
- [Pydantic AI](https://github.com/astral-sh/pydantic-ai) - AI agent framework
- [Together.ai](https://www.together.ai/) - AI model access
- [Logfire](https://logfire.dev/) - Observability platform

---

## ⚠️ Important Notes

- **Never commit your `.env` file** - it contains sensitive API keys
- **API Costs**: Be mindful of OpenRouter usage charges
- **Rate Limits**: Respect OpenRouter's rate limiting policies
- **Data Privacy**: Don't include sensitive information in task descriptions

---

## 🐛 Troubleshooting

### Common Issues

**ImportError: No module named 'pydantic_ai'**
```bash
pip install pydantic-ai
```

**API Key not found**
- Ensure your `.env` file is in the root directory
- Check that `OPENROUTER_API_KEY` is spelled correctly
- Verify your API key is valid on OpenRouter

**Model not supported error**
- Use one of the supported models listed above
- Check OpenRouter for model availability

### Getting Help

If you encounter issues:
1. Check the error logs in Logfire
2. Verify your API key and model availability
3. Open an issue with detailed error information

---

*Happy task parsing! 🚀*
