import time
import random
from tkinter import simpledialog

def ask_question(question, answer):
    while True:
        item = simpledialog.askstring("Question", question)
        if item is None:
            exit()
        if item == answer:
            print(item)
            break
    time.sleep(3)
    

while True:
    while True:
        x = random.randint(0, 2)

        if x == 0:
            ask_question("Type 'a':", "a")
    
        if x == 1:
            ask_question("Type 'b':", "b")

        if x == 2:
            ask_question("Type 'c':", "c")