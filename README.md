# Rasa-chatbot
This repository contains all code for a website and associated chatbot I built. The chatbot is made using [Rasa](https://rasa.com/), an open-source machine learning framework for conversational AI. To use the Rasa chatbot on the website, a widget is used from [this Github repository](https://github.com/botfront/rasa-webchat). 

There are 3 things which need to be run in a command prompt in order to view the website and associated chatbot in a web browser:
- Rasa models
- Rasa action server
- Flask server.

TO DO: make a requirements.txt file. Includes openpyxl, pandas, flask, babel, ...

# To run
Clone the repository in a local directory. Create a virtual environment inside this local directory (on Windows, this can be done by typing `python -m venv env`). 

To run the Rasa models, do the following in a command prompt window:
- activate the virtual environment (on Windows, this is done by typing `env\Scripts\activate` from the local directory)
- `cd rasa`
- `rasa run -m models --enable-api --cors "*" --debug`

To run the Rasa action server, do the following in another command prompt window:
- activate the virtual environment
- `cd rasa`
- `rasa run actions`

To run the Flask server from this local directory, do the following in another command prompt window:
- activate the virtual environment from the local directory
- `python app.py`

The website can then be viewed in a web browser at localhost:5000.
