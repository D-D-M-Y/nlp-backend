# Python file to call OpenAI API

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print(f"Using API Key: {api_key}")

OpenAI.api_key = api_key

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "system", "content": "Perform assistance for creation of a centralized wiki."},
    {"role": "assistant", "content": "I am Open Lexica, the AI-powered wiki assistant. What are your goals?"},
    {"role": "user", "content": "I am currently working on a software development project"},
    {"role": "assistant", "content": "Okay, who is this wiki for?"},
    {"role": "user", "content": "For my software development team, myself included"},
    {"role": "assistant", "content": "Okay, are there any specific sections that you already have in mind?"},
    {"role": "system", "content": "Perform analysis to the goals presented in the User role."},
    {"role": "system", "content": "Generate a wiki based on the analysis and present to the User role."},
    {"role": "assistant", "content": "Do you have any further requirements or suggestions?"}
  ]
)