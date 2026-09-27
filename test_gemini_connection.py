import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Describe the functional specification for an 8-bit synchronous counter with asynchronous reset, in 3 sentences."
)

print("Gemini connection successful!")
print("Response:")
print(interaction.output_text)