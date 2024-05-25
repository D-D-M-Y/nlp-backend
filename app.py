from flask import Flask, request, jsonify
#from flask_api import status
from flask_cors import CORS, cross_origin
from chatbotModule.userChatBotChat import gen_response, preprocess, predict, greet
from open_ai.api_caller import *
app = Flask(__name__)
CORS(app)

app.config.from_pyfile('settings.py')
app.config['CORS_HEADERS'] = 'Content-Type'


app.config.from_pyfile('settings.py')


@app.route("/")
def helloWorld():
    return "Hello World"

@app.route("/openlexica/get_response")
@cross_origin()
def openLexica():
    data = request.form
    if "context" in data:
        response = make_api_call(data["context"])
        headers = parse_list(response)
        generate_md_files(headers)
    return "No context provided", 400


@app.route("/openlexica/greet", methods=['GET'])
@cross_origin()
def greet_lexica():

    """
    A greeting message from OpenLexica

    Return:
    greeting (str): returns a json greeting string
    """
    greeting = greet()
    response = jsonify({
        "res": f"{greeting}",
        "sender": "backend"
    })
    repsonse.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/openlexica/response", methods=['POST'])
@cross_origin()
def chat_with_lexica():
    """
    The main chatting module for openlexica. Takes in a user input from a chat request and returns a response to the user.

    Return:
    chatresponse (str): A string response to a user input. 
    
    company (str): A string value containing a chat object for a user request on the type of company a user has. 
    For company wiki context.

    goal (str): A string value containing a chat object for a user request on the type of goal the user has. 
    For company wiki context.

    audience (str): A string value containing a chat object for a user request on the audience the company wiki needs.
    For company wiki context.

    structure (str): A string value containing a chat object for a user request on the structure the company wiki needs.
    For company wiki context.
    """
    data = request.form
    input_chat = preprocess(data["chat"])
    pred, check = predict(input_chat)
    if all(prob < 0.30 for prob in check):
        return jsonify({
            "res": f"I don't understand your request of {data["chat"]}",
            "sender": "backend"
        })
    company, goal, audience, structure = "", "", "", ""
    context_c, context_g, context_a, context_s = False, False, False, False
    print(data)
    print(type(data["company"]))
    if "company" in data and data["company"] != '':
        company = data["company"]
        context_c = True
    if "goal" in data and data["goal"] != '':
        goal = data["goal"]
        context_g = True
    if "audience" in data and data["audience"] != '':
        audience = data["audience"]
        context_a = True
    if "structure" in data and data["structure"] != '':
        structure = data["structure"]
        context_s = True

    if False:
        # context = data["company"] + data["goal"] + data["audience"] + data["structure"]
        # interact_with_lexica(context)
        print("hello")

    if pred == 'company':
        company = data["chat"]
    if pred == 'goal':
        goal = data["chat"]
    if pred == 'audience':
        audience = data["chat"]
    if pred == 'structure':
        structure = data["chat"]
    lexica_response = gen_response(pred)
    response = jsonify({
            "res": {
                "chatresponse": f"{lexica_response}",
                "company": company if context_c or company != '' else None,
                "goal": goal if context_g or goal != ''else None,
                "audience": audience if context_a or audience != '' else None,
                "structure": structure if context_s or structure != ''  else None,
            },
            "sender": "backend"
        })
    repsonse.headers.add('Access-Control-Allow-Origin', '*')

    return response
