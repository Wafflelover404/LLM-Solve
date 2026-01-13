# LLM-Solve: Automatic C++ Solution Generator

A Python script that automatically generates C++ solutions for competitive programming problems using AI models.

## Features

- 🤖 **AI-Powered**: Uses LLM Arena and other providers to find the best coding models
- 📝 **Problem Statement Integration**: Reads problems from `statement.md`
- ⚡ **Optimized C++**: Generates fast, competitive programming ready code with optimizations
- 🔄 **Multiple Providers**: Falls back between different AI providers
- 📊 **Response Logging**: Saves all generated solutions to `response.md`

## Setup

### Quick Setup (5 minutes)

1. **Install dependencies**:
```bash
pip3 install -r requirements.txt
```

2. **Get an API Key** (recommended - DeepSeek):
   - Go to [DeepSeek Platform](https://platform.deepseek.com/)
   - Sign up for free account
   - Get your API key from dashboard

3. **Configure API Key**:
```bash
cp config.example.py config.py
# Edit config.py and add your DeepSeek API key
```

4. **Run the generator**:
```bash
python3 run_g4f.py
```

### Alternative Providers

You can also use:
- **Claude Sonnet**: [Anthropic Console](https://console.anthropic.com/) ($5 free credit)
- **GPT-4**: [OpenAI Platform](https://platform.openai.com/) ($5 free credit)
- **Groq**: [Groq Console](https://console.groq.com/) (free tier, very fast)

## Configuration

### Quick Setup

1. **Add API Keys** to `config.py`:
```python
# Best for coding - Claude Sonnet
ANTHROPIC_API_KEY = "your-key-here"

# Specialized coding model
DEEPSEEK_API_KEY = "your-key-here"

# Strong general coding
OPENAI_API_KEY = "your-key-here"

# Fast inference
GROQ_API_KEY = "your-key-here"

# Multiple models access
OPENROUTER_API_KEY = "your-key-here"

# CodeLlama access
TOGETHER_API_KEY = "your-key-here"
```

2. **Provider Priority** (edit in `config.py`):
```python
PROVIDER_PRIORITY = [
    "anthropic_claude",     # Claude Sonnet - best for coding
    "deepseek_api",         # DeepSeek Coder - coding specialist
    "openai_gpt4",         # GPT-4 - strong general coding
    "groq_mixtral",        # Fast Mixtral
    "openrouter_claude",     # Claude via OpenRouter
    "together_codellama",   # CodeLlama
]
```

### Getting API Keys

- **Claude Sonnet**: [Anthropic Console](https://console.anthropic.com/)
- **DeepSeek Coder**: [DeepSeek Platform](https://platform.deepseek.com/)
- **GPT-4**: [OpenAI Platform](https://platform.openai.com/)
- **Groq Mixtral**: [Groq Console](https://console.groq.com/)
- **OpenRouter**: [OpenRouter AI](https://openrouter.ai/)
- **Together AI**: [Together AI](https://together.ai/)

### Supported Providers

#### Primary Coding Models:
- **🥇 Claude Sonnet** (Anthropic) - Best overall for coding
- **🥈 DeepSeek Coder** - Specialized competitive programming
- **🥉 GPT-4** (OpenAI) - Strong general coding capabilities
- **⚡ Groq Mixtral** - Fast inference for quick iterations
- **🌐 OpenRouter Claude** - Alternative Claude access
- **🦙 Together CodeLlama** - Open-source coding model

#### Fallback System:
- **g4f LLM Arena** (when Python 3.10+ compatible)
- **Direct API calls** (when g4f unavailable)
- **Template fallback** (when all APIs fail)

The system automatically tries providers in priority order and falls back gracefully.

## File Structure

```
LLM-Solve/
├── run_g4f.py          # Main generator script
├── config.py           # API keys and provider configuration
├── statement.md        # Problem statement input
├── solve.cpp           # Generated C++ solution
├── response.md         # Log of all generated solutions
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Usage Example

1. Edit `statement.md` with your problem:
```markdown
# Problem Statement

Given two integers a and b, print their sum.

## Input Format
Two space-separated integers a and b.

## Output Format
Print the sum of a and b.

## Sample Input
3 5

## Sample Output
8
```

2. Run the script:
```bash
python3 run_g4f.py
```

3. Check `solve.cpp` for the generated solution.

## Generated Code Features

- ✅ Fast I/O with `ios_base::sync_with_stdio(false)`
- ✅ GCC optimizations for competitive programming
- ✅ Clean, readable code structure
- ✅ Proper error handling
- ✅ C++17 compatible

## Troubleshooting

### g4f Compatibility Issues
The script automatically detects when g4f has compatibility issues (common with older Python versions) and falls back to direct API calls.

### API Issues
If external APIs fail, the script automatically falls back to a basic template.

### Dependencies
Make sure you have Python 3.7+ and all required packages installed.

### Python Version Compatibility
The script uses a hybrid approach:
- **Python 3.10+**: Uses g4f LLM Arena provider
- **Older versions**: Falls back to direct API calls
- **All versions**: Template fallback when APIs fail
