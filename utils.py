import urllib.request
import json

def ask(prompt: str, model: str = "llama3.2", temperature: float = 0.0) -> str:
    """Call the local Ollama model. Temperature 0 so that every run gives the same answers."""
    url = "http://localhost:11434/api/generate"
    data = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode("utf-8"))
        return res.get("response", "")

def count_tokens(text: str) -> int:
    return len(text.split())