# ╔═════════════════════════════════╗
# ║         📁 Python Project 📁
# ║
# ║  ✨ Team Members ✨
# ║
# ║  🧑‍💻 Elyasaf Cohen 311557227 🧑‍💻
# ║  🧑‍💻 Eldad Cohen   207920711 🧑‍💻
# ║  🧑‍💻 Israel Shlomo 315130344 🧑‍💻
# ║
# ╚══════════════════════════════════╝

# ╔════════════════════════════════════════════════╗
# ║     🤖 OLlama API Integration File 🤖          ║
# ║                                                ║
# ║  This file defines a helper function to send   ║
# ║  a prompt to a local Ollama model (like Mistral║
# ║  or LLaMA) and return its response.            ║
# ╚════════════════════════════════════════════════╝

import requests  # For sending http requests via internet or to local service


# ================================================================================= #
# A function that sends a text prompt to a locally running LLM model with Ollama,   #
# and returns the response we got back 📩                                           #
# ================================================================================= #
import requests

def ask_ollama(prompt: str, model="gemma:2b") -> str:
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        data = res.json()

        # נבדוק אם יש שדה של שגיאה
        if "error" in data:
            return f"❌ Ollama Error: {data['error']}"

        # נבדוק אם יש בכלל שדה בשם response
        if "response" not in data:
            return f"❌ Unexpected reply format: {data}"

        return data["response"]

    except Exception as e:
        return f"❌ Exception: {e}"

