# Trek Siri
A travel assistant chatbot using rasa nlu to answer frequently asked questions of travelers about different cities of Northern Pakistan.

## Getting Started
Download the whole project on your local machine and then run the following commands on three different command prompts
```
rasa run actions
```
After this run
```
rasa run -m models --enable-api --cors "*"
```
Finally to run the front-end, run the following command
```
python app.py
```
Go to the localhost link given by running the last command and ask the chatbot questions like "What is the weather in gilgit" or "Find me the best hotels in skardu".

### Prerequisites
You will need to install rasa-nlu and flask to run this project.
```
pip install rasa-nlu
```
```
pip install flask
```
