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
  Parses text to extract numbered list items as titles.

  Args:
    text (str): The text to parse.

  Returns:
    list: A list of titles extracted from numbered list items, 
         or None if no list is found.
  """
  # Regex pattern for numbered list items (capturing only the title)
  pattern = r"(^\d+\. )([^:]+)"  # Matches number followed by a dot and captures everything until colon
  titles = []
  matches = re.findall(pattern, text, re.MULTILINE)
  if matches:
    titles.extend([match[1].strip() for match in matches])
    return titles
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
        {"role": "system", "content": "You will assist people by making them a centralized wiki."},
        {"role": "system", "content": "Introduce yourself to the User role as Open Lexica, the AI-powered wiki assistant."},
        {"role": "system", "content": "Ask the User role their goals."},
        {"role": "system", "content": "Ask the User role who the wiki is for."},
        {"role": "system", "content": "Ask the User role for any specific sections they would like to include in the wiki."},
        {"role": "system", "content": "Analyze the goals presented by the User role and generate a wiki akin to a structured list with a numbered header ending with a colon and avoid using forward slashes, then present it to the User role."},
        {"role": "system", "content": "If the wiki is generated, ask the User role for any further requirements or suggestions they would like."},
      ]
    )
    lexica_says = response.choices[0].message.content
    print("Open Lexica:", lexica_says.strip("\n").strip())
    chat_log.append({"role": "assistant", "content": lexica_says.strip("\n").strip()})
    
# Parse response for lists and create markdown files
    titles = parse_list(lexica_says)
    if titles:
      for title in titles:
        filename = f"{title}.md"
        # Create the "files" directory if it doesn't exist
        os.makedirs("files", exist_ok=True)  # exist_ok=True prevents errors if it already exists
        filepath = os.path.join("files", filename)
        # Create empty markdown file
        with open(filepath, "w") as f:
          pass  # Empty file