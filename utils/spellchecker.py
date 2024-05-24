from spellchecker import SpellChecker
import nltk
from nltk.tokenize import word_tokenize

# Initialize SpellChecker
spell = SpellChecker()

def correct_spelling(text):
    """
    Corrects spelling errors in the input text using SpellChecker.

    Args:
    text (str): Input text to correct.

    Returns:
    str: Corrected text.
    """
    corrected_words = []
    for word in word_tokenize(text):
        corrected_word = spell.correction(word)
        if corrected_word is None:
            corrected_word = word  # If no correction found, keep the original word
        corrected_words.append(corrected_word)
    return ' '.join(corrected_words)
