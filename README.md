# FAQ_Chatbot_Project
This is an assignment for SC348810 - Software Development and Project Management for DSAI (Semester 1/2567)

## Milestone 1

Design the pipeline to execute the questions about the university information as well as respond the related answers

1. The Initial Setup:
### Create a virtual environment:
  - $ cd FAQ_Chatbot_Project
  - $ python3 -m venv venv
  - $ . venv/bin/activate

### Install dependencies:
  - $ (venv) pip install Flask torch torchvision nltk

### Install nltk package
  - $ (venv) python
  - $ import nltk
  - $ nltk.download('punkt')

### Run
  - $ (venv) python train.py
  This will dump data.pth file. And then run the following command to test it in the console.

  - $ (venv) python chat.py

## Milestone 2