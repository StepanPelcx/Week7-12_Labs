from openai import OpenAI
import os
from dotenv import load_dotenv


#Loan API key from enviroment variable
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Context-aware prompt

messages = [
    {"role": "system", "content": "You are a helpful Python assistant."},
    {"role": "user", "content": "Write an explanation of API for beginners."},
    {"role": "assistant", "content": "API is a ..."}
]

#Call OpenAI API
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

#Print the response
#Print(response.choices[0].message["content"])
print(response.choices[0].message.content)