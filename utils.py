import urllib.request
import json

def ask(prompt: str, model: str = "llama3.2") -> str:
    url = "http://localhost:11434/api/generate"
    data = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode("utf-8"))
        return res.get("response", "")

def count_tokens(text: str) -> int:
    return len(text.split())