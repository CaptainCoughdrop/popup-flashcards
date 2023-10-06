import time
import random
from tkinter import simpledialog

while True:
    while True:
        x = random.randint(0, 2)

        if x == 0:
            item = simpledialog.askstring("Question", "Type 'a':")
            while True:
                if item == "stop":
                    exit()
                if item == "a":
                    print(item)
                    break
                else:
                    item = simpledialog.askstring("Question", "Type 'a':")
            time.sleep(3)
            break
    
        if x == 1:
            item = simpledialog.askstring("Question", "Type 'b':")
            while True:
                if item == "stop":
                    exit()
                if item == "b":
                    print(item)
                    break
                else:
                    item = simpledialog.askstring("Question", "Type 'b':")
            time.sleep(3)
            break

        if x == 2:
            item = simpledialog.askstring("Question", "Type 'c':")
            while True:
                if item == "stop":
                    exit()
                if item == "c":
                    print(item)
                    break
                else:
                    item = simpledialog.askstring("Question", "Type 'c':")
            time.sleep(3)
            break