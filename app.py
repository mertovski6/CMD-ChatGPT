import openai
import os

openai.api_key = "OPENAI_API_KEY"  # ENTER YOUR API KEY HERE

def chat(prompt, model, temperature=0.6, max_tokens=500, top_p=1, frequency_penalty=0, presence_penalty=0):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )

    message = response.choices[0].text.strip()
    return message

print("Hello! Welcome to ChatGPT. Type something to chat. Type 'exit' to end the chat")

while True:
    user_input = input("YOU: ")

    if user_input.lower() == "exit":
        break

    response = chat(user_input, "text-davinci-003", temperature=0.6, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0)
    print("ChatGPT: " + response)