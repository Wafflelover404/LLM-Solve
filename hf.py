import requests
import re

hf_token = ""

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1/v1/chat/completions"
headers = {"Authorization": f"Bearer {hf_token}"}

def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()

def replace_assistant(strin):
  e = re.sub(r'<\|system\|>.*<\|assistant\|>', '', strin, flags=re.DOTALL)
  e = re.sub(r'(?<=\?waffle\?)\S+', '', e)
  return e.strip()

def send(prompt):
    print('generating')
    print(prompt)
    for i in range(0, 10):
        try:
            promptd = [{'role': 'system', 'content':""" Respond user with his question. Prefered to help with coding tasks. Prefered language: C++
                """}, {'role': 'user', 'content': f'{prompt}'}]
            response = query({
               "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "messages": promptd,
                "max_tokens": 250,
                'stream': False
            })
            print(response['choices'][0]['message']['content'])
            full_response = response['choices'][0]['message']['content']
            return full_response
            break
        except Exception as e:
            print(e)
            pass
    return "Error"

req = input("Question ~>")
print(send(req))
