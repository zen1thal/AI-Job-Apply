# Linkedin, Infojobs, Indeed Job Apply Bot

No time to be sitting for the entire day applying for jobs? No problem, this script might help you with the issue

## Progress

The code development is still in progress and it's made only for research reasons. It is planned to add later local
AI functionality model to respond custom questions that are outside of the algorithm. Any contributions would pretty
appreciated since the idea of this project consists of learning Python libraries while working with AI models.

## Requirements

- Install the same version of Chrome and ChromeDriver. Watch compatibilities here: https://developer.chrome.com/docs/chromedriver/downloads
- Python version 3.9+

## Setup

Update the config.json:

```json
username: # Insert your username here
password: # Insert your password here

keywords:
- # positions you want to search for
- # Another position you want to search for
- # A third position you want to search for

location:
- # Location you want to search for

Chrome User Directory:
- # Example MacOS: /Users/name_of_the_user/Library/Application Support/Google/Chrome

Profile:
- # Current Chrome Profile
```


Used Python 3.9.4 on MacOS via Virtual Environment/Conda

Before running, install the necessary libraries

```bash
pip3 install -r requirements.txt
```

## Execute

To execute the bot run the following in your terminal
```
python3 main.py
```
