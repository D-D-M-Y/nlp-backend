from flask import Flask
from open_ai.api_caller import interact_with_lexica

app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route("/")
def helloWorld():
    return "Hellow World"

@app.route("/jude")
def openLexica():
    while True:
        user_input = input("Your message: ")
        
        if user_input.lower() == "bye":
            print("Goodbye!")
            break
        
        # Call the function from the imported module
        interact_with_lexica(user_input)
        
if __name__ == "__main__":
    openLexica()

