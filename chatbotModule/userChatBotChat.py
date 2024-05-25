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
from sklearn.naive_bayes import MultinomialNB

stopwords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

with open('pickle/naivebayes.pkl', 'rb') as f:
   NaiveBayes = pickle.load(f)
with open('pickle/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)
with open('pickle/textvect.pkl', 'rb') as f:
    textVect = pickle.load(f)
with open("chatbotModule/responses.json",encoding='utf-8') as f:
    data = json.load(f)

def preprocess(input_string):
     input_string = " ".join([lemmatizer.lemmatize(word.lower()) for word in word_tokenize(input_string) if word.lower() not in stopwords and word not in punctuation])
     input_string = textVect.transform([input_string])
     return input_string

def predict(input_text_vect):
    check = NaiveBayes.predict_proba(input_text_vect)
    print(check)
    check = [x for inner_check in check for x in inner_check]
    result = NaiveBayes.predict(input_text_vect)
    result = label_encoder.inverse_transform(result)[0]
    return result, check
    
def gen_response(string):
    response = None
    for x in data["intents"]:
        if x["tag"] == string:
            response = random.choice(x["response"])
            if "follow-up" in x:
                follow_up = random.choice(x["follow-up"])
                return response,follow_up
            else:
                return response


def greet():
    intro_message = """Hello, I'm OpenLexica, an AI powered Wiki Creation Tool\n
                       I understand you're looking to create a wiki\n
                       Can we start by asking for the type of company or team you're looking to create a wiki for?"""
    return intro_message
        
