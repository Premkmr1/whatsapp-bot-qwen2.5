from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt")
    result = subprocess.run(["ollama", "run", "qwen:7b", prompt], capture_output=True, text=True)
    return jsonify({"response": result.stdout.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
