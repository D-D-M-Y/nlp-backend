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
            
def make_api_call2(header_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages= [
            {"role": "system", "content": "You are Open Lexica, the AI-powered wiki assistant and you will assist people by generating wiki content."},
            {"role": "system", "content":f"Generate relevant content for the {header_text}. Do not generate additional messages outside of the relevant content."},
        ]
    )
    lexica_says = response.choices[0].message.content
    return lexica_says  

def generate_md_files(headers):
    folder_name = "files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for header in headers:
        header_text = header.strip().strip(':')
        filename = os.path.join(folder_name, f"{header_text}.md")
        #choice = input(f"Do you want to generate a Markdown file for '{header_text}'? (y/n): ")
        #if choice.lower() == 'y':
        content = make_api_call2(header_text)
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Markdown file '{filename}' generated successfully.")
        #else:
        #    print(f"No Markdown file generated for '{header_text}'.")

if __name__ == "__main__":
    while True:
        user_message = input()
        if user_message.lower() == "bye":
            break
        else:
            interact_with_lexica(user_message)
