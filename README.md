# LLM
Long Language Model

# Encender ollama
```
ollama serve
```


# Solicitud a una API Rest
```
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"What is waos?",
  "stream":false
}'
```