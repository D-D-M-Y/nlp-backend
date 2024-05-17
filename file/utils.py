import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

def tokenize_text(text):
    """
    Function to tokenize the input text into words.

    Parameters:
    text (str): Input text to tokenize.

    Returns:
    list: List of words (tokens).
    """
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens

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
    # Initialize Sentiment Intensity Analyzer
    sid = SentimentIntensityAnalyzer()
    # Get polarity scores of the text
    scores = sid.polarity_scores(text)
    # Return the compound score, which represents overall sentiment
    return scores['compound']
