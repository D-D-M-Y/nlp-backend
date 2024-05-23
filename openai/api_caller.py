import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("AI_API_SECRET_KEY")
)

# variable to store api chat
chat_log = []

# Function for List Parser
def parse_list(text):
    """
    Parses text to extract numbered list items as titles and their dashed bullet points as content.

    Args:
        text (str): The text to parse.

    Returns:
        dict: A dictionary containing titles as keys and a list of contents as values.
    """
    pattern = r"(\d+\.\s+)(.*?)(?=\d+\.\s+|$)"  # Matches numbered headers
    matches = re.findall(pattern, text, re.DOTALL)
    parsed_list = {}
    for match in matches:
        header = match[0].strip()
        content = match[1].strip()
        sub_items = [item.strip() for item in content.split("-") if item.strip()]  # Split by dashes
        parsed_list[header] = sub_items
    return parsed_list

# Function for API Caller
def make_api_call(user_message):
    """
    Makes a call to the OpenAI API to get a response.

    Args:
        user_message (str): The user's message.

    Returns:
        str: The assistant's response.
    """
    global chat_log
    chat_log.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=chat_log + [
            {"role": "system", "content": "You will assist people by making them a centralized wiki."},
            {"role": "system", "content": "Introduce yourself to the User role as Open Lexica, the AI-powered wiki assistant."},
            {"role": "system", "content": "Ask the User role their goals."},
            {"role": "system", "content": "Ask the User role who the wiki is for."},
            {"role": "system", "content": "Ask the User role for any specific sections they would like to include in the wiki."},
            {"role": "system", "content": "Analyze the goals presented by the User role and generate a wiki akin to a structured list with a numbered header ending with a colon, avoid using forward slashes, and only use a dash (-) for the children of the headers, then present it to the User role."},
            {"role": "system", "content": "If the wiki is generated, ask the User role for any further requirements or suggestions they would like."},
        ]
    )
    lexica_says = response.choices[0].message.content
    chat_log.append({"role": "assistant", "content": lexica_says.strip("\n").strip()})
    return lexica_says.strip("\n").strip()

while True:
    user_message = input()
    if user_message.lower() == "bye":
        break
    else:
        response = make_api_call(user_message)
        print("Open Lexica:", response)

        # Parse response for lists and create markdown files
        parsed_list = parse_list(response)
        if parsed_list:
            for title, contents in parsed_list.items():
                filename = f"{title.replace(':', '')}.md"  # Remove colon from filename
                os.makedirs("files", exist_ok=True)
                filepath = os.path.join("files", filename)
                with open(filepath, "w") as f:
                    f.write('\n'.join(contents))

# Save chat log to a file when user responds with "bye"
chat_filepath = os.path.join("files", "chat_log.txt")
with open(chat_filepath, "w") as f:
    for entry in chat_log:
        f.write(f"{entry['role']}: {entry['content']}\n")
