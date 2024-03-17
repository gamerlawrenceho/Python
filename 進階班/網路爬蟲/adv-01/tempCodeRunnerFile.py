from tkinter import *

def hi_fun():
    print("Hello Singular")

win = Tk()
win.title("My first GUI")

btn = Button(win, text="Click Me", command=hi_fun, fg="#FF00FF", bg="#00FFFF")
btn.pack()

haha = Label(win, text="hi, I'm Python", fg="#FF00FF", bg="#00FFFF")
haha.pack()
lala = config(text="Hi singular", fg="red", bg="black")

from tkinter import *
import random as r


def show_fun():
    global clear
    display.config(text="Hi Singular", fg=color[r.randint(0, len(color) - 1)])
    print("Hello Singular")
    if clear == True:
        display.config(text="", fg="white", bg="white")
    else:
        display.config(text="Hi Singular", fg="red", bg="black")
    clear = not (clear)


def clear_fun():
    print("Hello Singular")
    display.config(text="", fg="white", bg="white")

clear = False
color = [
    "black", "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "brown", "gray"
]
windows = Tk()
windows.title("My first GUI")

btn1 = Button(windows, text="Show Screen", command=show_fun)
btn1.pack()

btn2 = Button(windows, text="Clear Screen", command=clear_fun)
btn2.pack()

display = Label(windows, text="")
display.pack()

windows.mainloop()

win.mainloop()
