import requests
import json 

"""
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"What is waos?",
  "stream":false
}'
"""

URI = "http://localhost:11434/api/generate"

data = {
    "model": "gemma3:1b",
    "prompt":"Hola",
    "stream":False,
}

response = requests.post(URI, json=data)

response = json.loads(response.text)

print(response['response'])


# TODO EJEMPLOS CON LOS DEMÁS MODELOS 
