import requests
import json
from dotenv import load_dotenv
import os

"""
curl -X POST "https://api.groq.com/openai/v1/audio/speech" 
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer ${GROQ_API_KEY}" 
      -d '{
         "model": "playai-tts",
         "voice": "Aaliyah-PlayAI",
         "input": "",
         "response_format": "wav"
       }' 
  --output out.wav
"""

load_dotenv(dotenv_path="key.env") 
api_key = os.getenv("GROQ_API_KEY")

URI = "https://api.groq.com/openai/v1/audio/speech"

data = {
    "model": "playai-tts",
    "voice": "Aaliyah-PlayAI",
    "input": "Welcome to Groq AI, the future of artificial intelligence.",
    "response_format": "wav"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(URI, headers=headers, data=json.dumps(data))


if response.status_code == 200:
    with open("out.wav", "wb") as f:
        f.write(response.content)
    print("Audio guardado como out.wav")
else:
    print("Error:", response.status_code)
    print("Respuesta:", response.text)
