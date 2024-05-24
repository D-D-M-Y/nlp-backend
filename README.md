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


# Modules Used

Flask. Flask serves as the foundation for building the web server that hosts our chatbot application. We use Flask to define routes, handle requests, and integrate the chatbot functionality seamlessly into the web interface.

json. We use the json module to handle the loading and parsing of JSON files. For example, we load the responses.json file, which contains chatbot responses and tags. 

pandas. The pandas module is essential for data manipulation and analysis. We leverage its capabilities to organize and process tabular data structures efficiently. In our backend, we use pandas for tasks such as loading and preprocessing data from JSON files.

pickle. For serialization and deserialization of Python objects, we rely on the pickle module. It enables us to save and load trained models, label encoders, and TF-IDF vectorizers. 

re (regex). The re module provides support for regular expressions, enabling advanced text pattern matching and manipulation.

scikit-learn (sklearn): Sklearn provides a comprehensive suite of machine learning algorithms and tools for data preprocessing, modeling, and evaluation. In our backend, we use sklearn for various tasks, including splitting data into training and testing sets, training classification models like Naive Bayes, and evaluating model performance using metrics such as accuracy and classification reports.

seaborn and matplotlib.pyplot. We use seaborn and matplotlib.pyplot to generate visualizations such as heatmaps for confusion matrices, enabling us to visualize model performance and identify areas for improvement.

NLTK. nltk is a crucial component of our backend for text processing. It provides various functions such as tokenization, stopword removal, and sentiment analysis. Tokenization involves breaking down the input text into individual words or sentences, making it easier to handle and analyze. Stopword removal filters out common words that do not contribute significantly to the meaning of the text, thereby focusing on the more informative words. Sentiment analysis uses NLTK to analyze the text and determine its sentiment, categorizing it as positive, negative, or neutral. These functionalities allows our application to effectively process and interpret textual data, enabling more sophisticated natural language understanding.

