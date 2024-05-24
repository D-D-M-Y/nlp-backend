from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from chatbotModule.userChatBotChat import gen_response, preprocess, predict, greet
from open_ai.api_caller import interact_with_lexica
app = Flask(__name__)
cors = CORS(app)

app.config.from_pyfile('settings.py')
app.config['CORS_HEADERS'] = 'Content-Type'


app.config.from_pyfile('settings.py')

@app.route("/")
def helloWorld():
    return "Hellow World"

@app.route("/jude")
@cross_origin()
def openLexica():
    while True:
        user_input = input("Your message: ")
        
        if user_input.lower() == "bye":
            print("Goodbye!")
            break
        
        # Call the function from the imported module
        interact_with_lexica(user_input)



@app.route("/openlexica/greet", methods=['GET'])
@cross_origin()
def greetLexica():
    greeting = greet()
    return jsonify({
        "res": f"{greeting}",
        "sender": "backend"
    })

@app.route("/openlexica/response", methods=['POST'])
@cross_origin()
def chatWithLexica():
    data = request.form
    input_chat = preprocess(data["chat"])
    pred, check = predict(input_chat)
    if all(prob < 0.30 for prob in check):
        return jsonify({
            "res": f"I don't understand your request of {data["chat"]}",
            "sender": "backend"
        })
    lexica_response = gen_response(pred)

    return jsonify({
            "res": f"{lexica_response}",
            "sender": "backend"
        })
