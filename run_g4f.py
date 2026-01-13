from g4f.client import Client
from g4f.Provider import Qwen, Perplexity, Ollama, AnyProvider
import time

def read_cpp_file(filename):
    """Read C++ file content"""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File {filename} not found"
    except Exception as e:
        return f"Error reading file: {e}"

def get_ai_response(code_content):
    """Get AI response for the code with fallback providers"""
    
    # Best free models in order of preference - Claude first
    model_providers = [
        # Claude models (highest priority)
        ("claude45sonnetthinking", Perplexity),
        ("claude40opusthinking", Perplexity),
        ("claude37sonnetthinking", Perplexity),
        ("claude2", Perplexity),
        
        # GPT models
        ("gpt41", Perplexity),
        ("grok4", Perplexity),
        
        # Top tier Qwen models
        ("qwen3-max-preview", Qwen),
        ("qwen3-235b-a22b", Qwen),
        ("qwen3-coder-plus", Qwen),
        ("qwen-max-latest", Qwen),
        
        # High quality models
        ("deepseek-v3.2", Ollama),
        ("qwen3-coder:480b", Ollama),
        
        # Reliable fallbacks
        ("qwen-3-235b", AnyProvider),
        ("qwen-3-32b", AnyProvider),
        ("qwen-2.5-72b", AnyProvider),
        ("command-r-plus-08-2024", AnyProvider),
        ("ling-flash-2.0", AnyProvider),
    ]
    
    prompt = f"""Please analyze this C++ code and provide a solution implementation:

{code_content}

Read the problem statement from statement.md and implement the solution accordingly.
Provide only the completed C++ code without explanations."""
    
    for model_name, provider in model_providers:
        try:
            print(f"Trying {model_name} with {provider.__name__}...")
            
            client = Client(provider=provider)
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                web_search=False
            )
            
            if hasattr(response, 'choices') and response.choices:
                message = response.choices[0].message.content
                if message and message.strip():
                    print(f"✓ Success with {model_name}!")
                    return message
            else:
                print(f"✗ Empty response from {model_name}")
                
        except Exception as e:
            print(f"✗ Error with {model_name}: {str(e)[:100]}...")
            continue
            
        # Small delay between attempts
        time.sleep(0.5)
    
    return "All providers failed. Please try again later or use an API key."

def main():
    """Main function"""
    print("Reading solve.cpp...")
    cpp_content = read_cpp_file("solve.cpp")
    
    print("Getting AI solution...")
    ai_response = get_ai_response(cpp_content)
    
    print("\n" + "="*50)
    print("AI SOLUTION:")
    print("="*50)
    print(ai_response)

if __name__ == "__main__":
    main()
    
