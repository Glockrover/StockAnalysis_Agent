import requests
import json
import os

# Get the API key from an environment variable
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENROUTER_API_KEY environment variable.")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1-zero:free",
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ],
    })
)

print(response.json())