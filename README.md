# FAQ_Chatbot_Project
This is an assignment for SC348810 - Software Development and Project Management for DSAI (Semester 1/2567)

## Milestone 1

Design the pipeline to execute the questions about the university information as well as respond the related answers

##The Initial Setup:
### Create a virtual environment:
  - $ cd FAQ_Chatbot_Project
  - $ python3 -m venv venv
  - $ . venv/bin/activate

### Install dependencies:
  - $ (venv) pip install Flask torch torchvision nltk

### Install nltk package:
  - $ (venv) python
  - $ import nltk
  - $ nltk.download('punkt')

### Run:
  - $ (venv) python train.py
  [This will dump data.pth file. And then run the following command to test it in the console.]

  - $ (venv) python chat.py

## Milestone 2

In this milestone 2 is the process of integrating user interface with the occurred pipeline from milestone 1. It covers the creation of a Flask app for making predictions, setting up routes, handling post requests, and returning responses. It also related to connecting Flask with JavaScript for interactive functionality.

### The starter folders for Frontend
  - static folder contains the files such as:
    - Images folder which has all the images needed for the Flask application
    - javascript file
    - css file for the styling
  - templates folder contains the base.html file
  - There is another app.py to execute the Flask app
  
