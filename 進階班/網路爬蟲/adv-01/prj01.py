# from tkinter import *

# def hi_fun():
#     print("Hello Singular")

# win = Tk()
# win.title("My first GUI")

# btn = Button(win, text="Click Me", command=hi_fun, fg="#FF00FF", bg="#00FFFF")
# btn.pack()

# haha = Label(win, text="hi, I'm Python", fg="#FF00FF", bg="#00FFFF")
# haha.pack()
# lala = config(text="Hi singular", fg="red", bg="black")

# from tkinter import *
# import random as r

# def show_fun():
#     global clear
#     display.config(text="Hi Singular", fg=color[r.randint(0, len(color) - 1)])
#     print("Hello Singular")
#     if clear == True:
#         display.config(text="", fg="white", bg="white")
#     else:
#         display.config(text="Hi Singular", fg="red", bg="black")
#     clear = not (clear)

# def clear_fun():
#     print("Hello Singular")
#     display.config(text="", fg="white", bg="white")

# clear = False
# color = [
#    "black",
#    "red",
#    "green",
#    "blue",
#    "yellow",
#    "orange",
#    "purple",
#    "pink",
#    "brown",
#    "gray",
#    "cyan",
#    "magenta",
#    "gold",
#    "silver",
#    "lime",
#    "maroon",
#    "navy",
#    "olive",
#    "teal",
#    "violet",
#    "indigo",
#    "coral",
#    "crimson",
#    "hotpink",
#    "khaki",
#    "lavender",
#    "lavenderblush",
#    "lemonchiffon",
#    "lightblue",
#    "lightcoral",
#    "lightcyan",
#    "lightgoldenrodyellow",
#    "lightgreen",
#    "lightgrey",
#    "lightpink",
#    "lightsalmon",
#    "lightseagreen",
#    "lightskyblue",
#    "lightslategray",
#    "lightsteelblue",
#    "lightyellow",
#]
# color = [

# windows.title("My first GUI")

# btn1 = Button(windows, text="Show Screen", command=show_fun)
# btn1.pack()

# btn2 = Button(windows, text="Clear Screen", command=clear_fun)
# btn2.pack()

# display = Label(windows, text="")
# display.pack()

# windows.mainloop()

# win.mainloop()

# import modules
'''
關機程式!!!!!!!!!!!!!
############## from tkinter import *
############## import os
#############
#############
############## # user define function
############## def shutdown():
############## 	return os.system("shutdown /s /t 1")
#############
############## def restart():
############## 	return os.system("shutdown /r /t 1")
#############
############## def logout():
############## 	return os.system("shutdown -l")
#############
#############
############## # tkinter object
############## master = Tk()
#############
############## # background set to grey
############## master.configure(bg='light grey')
#############
############## # creating a button using the widget
############## # Buttons that will call the submit function
############## Button(master, text="Shutdown", command=shutdown).grid(row=0)
############## Button(master, text="Restart", command=restart).grid(row=1)
############## Button(master, text="Log out", command=logout).grid(row=2)
#############
############## mainloop()
'''
from tkinter import *
import random as r


def show_fun():
    global clear
    display.config(text="Hi Singular", fg=color[r.randint(0, len(color) - 1)])
    # print("Hello Singular")
    # if clear == True:
    #     display.config(text="", fg="white", bg="white")
    # else:
    #     display.config(text="Hi Singular", fg="red", bg="black")
    # clear = not (clear)


# def clear_fun():
#     print("Hello Singular")
#     display.config(text="", fg="white", bg="white")

clear = False
color = [
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "lime",
    "maroon",
    "navy",
    "olive",
    "teal",
    "violet",
    "indigo",
    "coral",
    "crimson",
    "hotpink",
    "khaki",
    "lavender",
    "lavenderblush",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightsteelblue",
    "lightyellow",
]
windows = Tk()
windows.title("My first GUI")

btn1 = Button(windows, text="Show Screen", command=show_fun)
btn1.pack()

# btn2 = Button(windows, text="Clear Screen", command=clear_fun)
# btn2.pack()

display = Label(windows, text="")
display.pack()

windows.mainloop()