import openai
import json

openai.api_key = "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" # Ganti YOUR_API_KEY dengan API key Anda

def ask(question, model, temperature=0.5):
    response = openai.Completion.create(
        engine=model,
        prompt=question,
        temperature=temperature,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response.choices[0].text != None:
        return response.choices[0].text.strip()
    else:
        return ""
