from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set!")

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

def ask_gemini(question):
    response = genai.chat.send_message(
        model="chat-bison-001",
        messages=[{"author": "user", "content": question}]
    )
    return response.last.message.content

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            answer = ask_gemini(question.lower().strip())
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
