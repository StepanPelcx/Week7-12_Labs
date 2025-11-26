from openai import OpenAI
from dotenv import load_dotenv
import os

# Initialize the OpenAI client with your API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a simple API call
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! What is AI?"}
    ]
)
# Print the response
print(completion.choices[0].message.content)
