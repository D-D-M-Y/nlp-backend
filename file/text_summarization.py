import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Downloads necessary NLTK resources if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')

def remove_stopwords(text):
    """
    Function to remove stopwords from the input text.

    Parameters:
    text (str): Input text to remove stopwords from.

    Returns:
    str: Text with stopwords removed.
    """
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    # Tokenize the text
    words = word_tokenize(text)
    # Filter out stopwords
    filtered_text = [word for word in words if word.lower() not in stop_words]
    # Join the filtered words back into a string
    return ' '.join(filtered_text)

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
