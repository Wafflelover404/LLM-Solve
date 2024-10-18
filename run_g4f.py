from g4f.client import Client

def generate_text(prompt):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = input("Enter your text prompt: ")
    generated_text = generate_text(prompt)
    f = open("response.md", "a")
    f.write(generated_text)
    f.close()
    print("Written Ai response to response.md")
