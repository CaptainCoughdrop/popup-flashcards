import time
import random
from tkinter import simpledialog
import json

with open('questions.txt') as f:
    data = f.read()
questions = json.loads(data)

def ask_question(question, answer):
    while True:
        item = simpledialog.askstring("Question", question)
        if item is None:
            exit()
        if item == "dict":
            for i in questions.items():
                for x in i:
                    print(x)
        if item == answer:
            print(item)
            break
    time.sleep(1)
    

while True:
    while True:
        questions_list = list(questions.items())
        random_question = random.choice(questions_list)
        ques, ans = random_question
        ask_question(ques, ans)