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

# =========== Load libraries ============ #
import requests
import os
from sentence_transformers import SentenceTransformer
from Fronted.Services.vector_store import load_data, create_faiss_index, search_similar_chunks

# =========== Base function: send prompt to Ollama ============ #
def ask_ollama(prompt: str, model="gemma:2b") -> str:
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        data = res.json()

        if "error" in data:
            return f"❌ Ollama Error: {data['error']}"
        if "response" not in data:
            return f"❌ Unexpected reply format: {data}"

        return data["response"]

    except Exception as e:
        return f"❌ Exception: {e}"

# =========== Load the chunks and embeddings using dynamic path ============ #
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, "Dataset", "embeddings.json")
chunks, embeddings = load_data(json_path)
index = create_faiss_index(embeddings)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# =========== Contextual LLM interaction ============ #
def ask_ollama_contextual(question: str, model_name="gemma:2b") -> str:
    # =========== Step 1: Create embedding for the question ============ #
    question_vec = embedding_model.encode([question])[0]

    # =========== Step 2: Search for the most relevant chunks ============ #
    relevant_chunks = search_similar_chunks(question_vec, index, chunks, top_k=5)

    # =========== Step 3: Create the full prompt for Ollama ============ #
    context = "\n".join(relevant_chunks)
    final_prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion: {question}"

    # =========== Step 4: Send the enriched prompt to Ollama ============ #
    return ask_ollama(final_prompt, model=model_name)
