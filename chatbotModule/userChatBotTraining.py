import json
import pandas as pd
import nltk
from string import punctuation
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

import seaborn as sns 
from matplotlib import pyplot as plt 

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('wordnet')

stopwords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()
label_encoder = LabelEncoder()

with open("chatbotModule/responses.json",encoding='utf-8') as file:
  data = json.load(file)

data2 = []

for x in data["intents"]:
    local_tag = x["tag"]
    for words in x["input"]:
        data2.append([local_tag, words])

df = pd.DataFrame(data2)

df.columns = ["Tag", "Input"]

label_encoder.fit(df["Tag"])

with open('pickle/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

df["clean_inputs"] = df["Input"].apply(lambda x: " ".join(lemmatizer.lemmatize(word.lower()) for word in word_tokenize(x) if word.lower() not in stopwords and word not in punctuation))
df["tag_inputs"] = df["Tag"].apply(lambda x: label_encoder.transform([x])).apply(lambda x: x[0])

textVect = TfidfVectorizer(stop_words="english")
textVect.fit({word for word in df["clean_inputs"]})

with open('pickle/textvect.pkl', 'wb') as f:
    pickle.dump(textVect, f)

x = df["clean_inputs"]
y = df["tag_inputs"]

x = textVect.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

x_train.toarray()

NaiveBayes = MultinomialNB()
NaiveBayes.fit(x_train, y_train)

with open('pickle/naivebayes.pkl', 'wb') as f:
    pickle.dump(NaiveBayes, f)

pred = NaiveBayes.predict(x_test)

print(accuracy_score(y_test, pred))