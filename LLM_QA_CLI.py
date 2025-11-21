# LLM_QA_CLI.py
import os
from dotenv import load_dotenv
from google.genai import Client, types

# Load your API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY ")

if not API_KEY:
    raise ValueError("Please set your GEMINI_API_KEY  in the .env file.")

# Initialize the client
client = Client(api_key=API_KEY)

def ask_gemini(question: str) -> str:
    """Send a question to Gemini and get the answer."""
    try:
        # Correct usage: Part.from_text() takes only 1 argument
        content = types.Part.from_text(question)

        response = client.models.generate_content(
            model="gemini-2.5-flash",  # Make sure this model exists
            contents=[content],
            config=types.GenerateContentConfig(
                temperature=0.2,
                max_output_tokens=200
            )
        )

        # Extract the answer text
        answer = response.result[0].content[0].text
        return answer

    except Exception as e:
        return f"Error calling Gemini: {e}"

def main():
    print("========= LLM QUESTION ANSWERING CLI =========")
    while True:
        user_input = input("Enter your question (or 'exit'): ").strip()
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        processed = user_input.lower()  # Simple preprocessing
        print(f"Processed: {processed}")
        print("Sending request to LLM...")
        answer = ask_gemini(processed)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    main()
