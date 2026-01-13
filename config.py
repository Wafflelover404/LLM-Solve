"""
Configuration file for LLM-Solve
Add your API keys here to enable different providers
"""

# Anthropic Claude Sonnet - Excellent for coding
ANTHROPIC_API_KEY = ""  # Get from https://console.anthropic.com/

# OpenAI GPT-4 - Strong coding capabilities
OPENAI_API_KEY = ""  # Get from https://platform.openai.com/

# DeepSeek Coder - Specialized for coding
DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_API_KEY_HERE"  # Get from https://platform.deepseek.com/

# Groq Mixtral - Fast inference
GROQ_API_KEY = ""  # Get from https://console.groq.com/

# OpenRouter - Access to multiple models
OPENROUTER_API_KEY = ""  # Get from https://openrouter.ai/

# Together AI - CodeLlama and other models
TOGETHER_API_KEY = ""  # Get from https://together.ai/

# Preferred provider order (first available will be used)
PROVIDER_PRIORITY = [
    "anthropic_claude",     # Claude Sonnet - best for coding
    "deepseek_api",         # DeepSeek Coder - coding specialist
    "openai_gpt4",         # GPT-4 - strong general coding
    "groq_mixtral",        # Fast Mixtral
    "openrouter_claude",     # Claude via OpenRouter
    "together_codellama",   # CodeLlama
]
