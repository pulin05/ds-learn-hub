import requests
import json

# Define the base URL for the Ollama server
base_url = "http://localhost:11434/api/generate"

headers = {"Content-type": "application/json"}

# The model you want to use (e.g., 'llama', 'alpaca')
model = "llama3.2"
query = "what is AI?"

data = {"model": model,
        "prompt": query,
        "stream": False}
# Your query


# Sending the request to Ollama
response = requests.post(base_url,headers=headers,json=data)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()['response']
    print("Response from Ollama:")
    print(data)
else:
    print(f"Failed to connect. Status code: {response.status_code}")
    print(response.text)
