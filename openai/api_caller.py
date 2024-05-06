# Python file to call OpenAI API

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key = os.environ.get("AI_API_SECRET_KEY")
)

OpenAI.api_key = client.api_key

chat_log = []

while True:
  user_message = input()
  if user_message.lower() == "bye":
    break
  else:
    chat_log.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-16k",
      messages= chat_log + [
        {"role": "system", "content": "Introduce yourself to the User role as Open Lexica, the AI-powered wiki assistant."},
        {"role": "system", "content": "Perform assistance for creation of a centralized wiki."},
        {"role": "system", "content": "Ask the User role their goals."},
        {"role": "system", "content": "Ask the User role who the wiki is for."},
        {"role": "system", "content": "Ask the User role for any specific sections they would like to include in the wiki."},
        {"role": "system", "content": "Analyze the goals presented by the User role and generate a wiki then present it to the User role."},
        {"role": "system", "content": "If the wiki is generated, ask the User role for any further requirements or suggestions they would like."},
      ]
    )
    lexica_says = response.choices[0].message.content
    print("Open Lexica:", lexica_says.strip("\n").strip())
    chat_log.append({"role": "assistant", "content": lexica_says.strip("\n").strip()})