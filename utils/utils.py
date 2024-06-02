import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')



def tokenize_text(text):
    """
    Function to tokenize the input text into words and correct spelling errors.

    Parameters:
    text (str): Input text to tokenize.

    Returns:
    list: List of words (tokens) with corrected spelling.
    """
    corrected_tokens = []
    for word in word_tokenize(text):
        corrected_word = spell.correction(word)
        if corrected_word is None:
            corrected_word = word  # If no correction found, it keeps the original word
        corrected_tokens.append(corrected_word)
    return corrected_tokens

def remove_stopwords(tokens):
    """
    Function to remove stopwords from a list of tokens.

    Parameters:
    tokens (list): List of words (tokens) to remove stopwords from.

    Returns:
    list: List of tokens with stopwords removed.
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return filtered_tokens

def sentiment_analysis(text):
    """
    Function to perform sentiment analysis on the input text.

    Parameters:
    text (str): Input text for sentiment analysis.

    Returns:
    float: Sentiment score of the text (ranges from -1 to +1).
    """

    sid = SentimentIntensityAnalyzer()

    scores = sid.polarity_scores(text)

    return scores['compound']

def get_title(directory):
    return [f[:-3] for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_content(filename):
    f = open(f"files/{filename}.md", 'r')
    s = f.read()
    f.close()
    return s