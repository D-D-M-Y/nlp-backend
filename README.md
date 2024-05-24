# Open Lexica Backend
A  server to run NLP processes of Open Lexica

## Backend
Open Lexica's backend is responsible for processing user input, generating content, performing text preprocessing, and conducting sentiment analysis. The backend also includes a file generator to create markdown files for the wiki.

# Installation
Prerequisites
Python 3.8 or higher
NLTK

## How to use
1. Install the environment from requirements.txt
2. Run the following code
```
python -m flask run
```
or
```
python -m flask --app .\app.py run
```
<br>
You need to set your own variables for running your API for AI to search the internet


Open Lexica is an application that generates a complete wiki in markdown files for your company using the power of language models.
-Use your input to generate a homepage wiki and a file directory for other wiki files.
-Input gathered from you will be used to query ChatGPT for content generation.
-Accessible and easy-to-share markdown format.
-Customizable and self-hostable for your specific needs.
-Open-source and community-driven development.


## Tokenization
Text tokenization splits text into meaningful units like words or phrases. This is essential for further text processing tasks such as stemming, lemmatization, and part-of-speech (POS) tagging.

## Preprocessing Steps
Stemming: Reduces words to their base or root form.
Lemmatization: Reduces words to their base or dictionary form.
POS Tagging: Identifies the part of speech for each word in the text.
Sentiment Analysis
The sentiment analysis component uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool from NLTK to return numerical values for sentiment. This helps in generating appropriate responses based on user input.

## Sentiment Scoring
Positive: Indicates positive sentiment.
Negative: Indicates negative sentiment.
Neutral: Indicates neutral sentiment.
