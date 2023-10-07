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
        if item == answer:
            print(item)
            break
    time.sleep(1)
    

while True:
    while True:
        questions_list = list(questions.items())
        ques, ans = random.choice(questions_list)
        ask_question(ques, ans)