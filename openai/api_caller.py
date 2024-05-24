import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("AI_API_SECRET_KEY")
)

chat_log = []

def make_api_call(user_message):
    global chat_log
    chat_log.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=chat_log + [
            {"role": "system", "content": "You are Open Lexica, the AI-powered wiki assistant and you will assist people by making them a centralized wiki by first introducing yourself and by asking them questions."},
            {"role": "system", "content": "Ask the User role what type of business they are running, their goals for the creation of the wiki, who the wiki is for, and if there are any specific sections they would like to include."},
            {"role": "system", "content": "Analyze the goals, the intended users, and the specific sections specified by the User role and generate a wiki akin to a structured list with a numbered header ending with a colon, avoid using forward slashes, and only use a dash (-) for the children of the headers, then present it to the User role."},
            {"role": "system", "content": "If the wiki is generated, ask the User role for any further requirements or suggestions they would like."},
        ]
    )
    lexica_says = response.choices[0].message.content
    chat_log.append({"role": "assistant", "content": lexica_says.strip("\n").strip()})
    return lexica_says.strip("\n").strip()

def parse_list(output):
    headers = re.findall(r'\d+\..+?:\n', output)
    return headers

def generate_md_files(headers):
    """
    Prompts the user if they want to generate Markdown files for each numbered header.

    Args:
        headers (list): The list of numbered headers.
    """
    folder_name = "files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for header in headers:
        header_text = header.strip().strip(':')
        filename = os.path.join(folder_name, f"{header_text}.md")
        
        if os.path.exists(filename):
            choice = input(f"Do you want to update the content of '{header_text}' Markdown file? (y/n): ")
            if choice.lower() == 'y':
                with open(filename, 'a') as file:
                    while True:
                        child_content = input(f"Enter content for a child of '{header_text}' (or 'done' to finish): ")
                        if child_content.lower() == 'done':
                            break
                        file.write(f"   - {child_content}\n")
                print(f"Content updated successfully for '{header_text}'.")
            else:
                print(f"No changes made to '{header_text}'.")
        else:
            with open(filename, 'w') as file:
                file.write(header)
                print(f"Markdown file '{filename}' generated successfully.")
                while True:
                    child_content = input(f"Enter content for a child of '{header_text}' (or 'done' to finish): ")
                    if child_content.lower() == 'done':
                        break
                    file.write(f"   - {child_content}\n")
                print(f"Content added successfully for '{header_text}'.")


while True:
    user_message = input()
    if user_message.lower() == "bye":
        break
    else:
        response = make_api_call(user_message)
        print("Open Lexica:", response)
        headers = parse_list(response)
        generate_md_files(headers)