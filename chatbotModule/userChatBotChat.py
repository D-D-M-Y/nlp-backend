import json
import nltk
import pickle
import random
from string import punctuation
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
import pickle 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

stopwords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

with open('pickle/decisiontree.pkl', 'rb') as f:
    DecisionTree = pickle.load(f)
with open('pickle/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)
with open('pickle/textvect.pkl', 'rb') as f:
    textVect = pickle.load(f)
with open("chatbotModule/responses.json",encoding='utf-8') as f:
    data = json.load(f)

def preprocess(input_string):
     input_string = " ".join([lemmatizer.lemmatize(word.lower()) for word in input_string.split() if input_string.lower() not in [stopwords, punctuation]])
     input_string = textVect.transform([input_string])
     return input_string

def predict(input_text_vect):
    result = DecisionTree.predict(input_text_vect)
    result = label_encoder.inverse_transform(result)[0]
    return result
    
def response(string):
    for x in data["intents"]:
        if x["tag"] == string:
            response = random.choice(x["response"])
    return response

while True:
    #Enter an input
    my_input = input()
    if my_input.lower() == "bye":
        break
    else:
        my_input = preprocess(my_input)
        pred = predict(my_input)
        chat_response = response(pred)
