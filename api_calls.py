import requests
import json
import openai
import config


def get_perplexity_data(prompt, temp, model_name):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": model_name,
        "temperature": temp,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f'''Bearer {config.perplexity_api_key}'''
    }

    response = requests.post(url, json=payload, headers=headers)
    return json.loads(response.text)["choices"][0]['message']['content'].strip()


def get_gpt4_data(prompt, temp):
    answer_response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temp,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    final_answer = answer_response.choices[0].message.content.strip()
    return final_answer
