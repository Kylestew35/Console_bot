import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("API key not found. Please set OPENAI_API_KEY in your .env file")

openai.api_key = api_key

def chatbot(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant. Provide detailed and accurate code examples and explanations."},
                {"role": "user", "content": query}
            ],
            max_tokens=2000,  # Large enough to handle long code outputs and explanations
            temperature=0.3,  # Lower temperature for more deterministic coding assistance
            top_p=0.9,  # Using typical sampling method
            frequency_penalty=0,  # No repetition penalty
            presence_penalty=0  # No penalty for introducing new topics
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to your OpenAI Coding Assistant! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()