import requests
import json

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
api_key = "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"

URI = "https://api.groq.com/openai/v1/audio/speech"

data = {
    "model": "playai-tts",
    "voice": "Aaliyah-PlayAI",
    "input": "Hola perdida!",
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
