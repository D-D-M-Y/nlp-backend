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

from sklearn.tree import DecisionTreeClassifier

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('wordnet')

stopwords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()
label_encoder = LabelEncoder()

with open("responses.json",encoding='utf-8') as file:
  data = json.load(file)

df = pd.json_normalize(data["intents"], meta=["tag", "input", "response"])

label_encoder.fit(df["tag"])

df["clean_inputs"] = df["input"].apply(lambda x: " ".join([lemmatizer.lemmatize(word.lower()) for word in x if word.lower() not in [stopwords, punctuation]]))
df["tag_inputs"] = df["tag"].apply(lambda x: label_encoder.transform([x])).apply(lambda x: x[0])