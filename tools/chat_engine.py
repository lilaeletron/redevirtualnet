import ollama
from joblib import PrintTime

client = ollama.Client(host="45.229.53.169:11434")

for model in client.list():
    print()