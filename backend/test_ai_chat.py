import requests

url = "http://127.0.0.1:8000/ai/chat"

payload = {
    "message": """
Today I met Dr. Paul at Apollo Hospital.

We discussed GlucoCare diabetes tablets.

He was interested in clinical trial results.

Please follow up next Tuesday.
"""
}

response = requests.post(url, json=payload)

print(response.json())