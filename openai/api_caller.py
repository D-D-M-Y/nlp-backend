# Python file to call OpenAI API

import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key = os.environ.get("AI_API_SECRET_KEY")
)

OpenAI.api_key = client.api_key

chat_log = []

def parse_list(text):
  """
  Parses text to extract a bulleted or numbered list.

  Args:
    text (str): The text to parse.

  Returns:
    list: A list of items extracted from the text, 
         or None if no list is found.
  """
  # Regex patterns for bulleted and numbered lists
  bullet_pattern = r"(?:^\s*[-*+•]\s+|^.+\s*[-*+•]\s+)(.*?)(?=\n|$)"
  numbered_pattern = r"(?:^\s*\d+\.\s+|^.+\s*\d+\.\s+)(.*?)(?=\n|$)"
  items = []
  for pattern in [bullet_pattern, numbered_pattern]:
    matches = re.findall(pattern, text, re.MULTILINE)
    if matches:
      items.extend([match.strip() for match in matches])
      return items
  return None

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
    
# Parse response for lists and update chat_log
    parsed_list = parse_list(lexica_says)
    if parsed_list:
      chat_log.append({"role": "assistant (parsed)", "content": parsed_list})

# Write chat log to file
filename = "chat_log.txt"
# Create the "files" directory if it doesn't exist
os.makedirs("files", exist_ok=True)  # exist_ok=True prevents errors if it already exists
filepath = os.path.join("files", filename)

with open(filepath, "w") as f:
  for entry in chat_log:
    f.write(f"{entry['role']}: {entry['content']}\n")

print(f"Conversation history saved to: files/{filename}")