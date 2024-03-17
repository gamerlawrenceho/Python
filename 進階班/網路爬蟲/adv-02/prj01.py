# #1.匯入 tkinter 模組和 random 模組
# from tkinter import *
# import random

# # 定義 hi_fun 函數，當按鈕被按下時，將標籤的文字設為 "Hi Singular"，前景顏色隨機選擇 COLORS 中的一種。
# def hi_fun():
#     display.config(text="Hi Singular", fg=random.choice(COLORS))

# # 定義 COLORS，為一個包含了多種顏色的列表
# COLORS = [
#     "black",
#     "red",
#     "green",
#     "blue",
#     "yellow",
#     "orange",
#     "purple",
#     "pink",
#     "brown",
#     "gray",
#     "cyan",
#     "magenta",
#     "gold",
#     "silver",
#     "lime",
#     "maroon",
#     "navy",
#     "olive",
#     "teal",
#     "violet",
#     "indigo",
#     "coral",
#     "crimson",
#     "hotpink",
#     "khaki",
#     "lavender",
#     "lavenderblush",
#     "lemonchiffon",
#     "lightblue",
#     "lightcoral",
#     "lightcyan",
#     "lightgoldenrodyellow",
#     "lightgreen",
#     "lightgrey",
#     "lightpink",
#     "lightsalmon",
#     "lightseagreen",
#     "lightskyblue",
#     "lightslategray",
#     "lightsteelblue",
#     "lightyellow",
# ]

# # 創建主視窗
# windows = Tk()

# # 設定主視窗標題
# windows.title("My first GUI")

# # 創建一個按鈕，當被按下時，執行 hi_fun 函數
# btn1 = Button(windows, text="Show Screen", command=hi_fun)

# # 將按鈕加入主視窗中
# btn1.pack()

# # 創建一個標籤，顯示 "Hi Singular"
# display = Label(windows, text="Hi Singular")

# # 將標籤加入主視窗中
# display.pack()

# # 開始執行主迴圈，等待用戶操作
# windows.mainloop()

# 2.from tkinter import *

# windows = Tk()
# windows.title("My First GUI")

# canvas = Canvas(windows, width=600, height=600, bg='lightskyblue')
# canvas.pack()

# windows.mainloop()

from tkinter import *
import sys
import os

os.chdir(sys.path[0])


def move_canvas(event):
    key = event.keysym
    print(key)
    if key == 'Right':
        canvas.move(circle, 10, 0)
    elif key == 'Left':
        canvas.move(circle, -10, 0)
    elif key == 'Up':
        canvas.move(circle, 0, -10)
    elif key == 'Down':
        canvas.move(circle, 0, 10)
    elif key == 'D':
        canvas.move(rect, 10, 0)
    elif key == 'A':
        canvas.move(rect, -10, 0)
    elif key == 'W':
        canvas.move(rect, 0, -10)
    elif key == 'S':
        canvas.move(rect, 0, 10)


def exit_fun():
    windows.destroy()


def exit_fun():
    windows.destroy()


windows = Tk()
windows.title("My First GUI")

quit_btn = Button(windows, text="Quit", command=exit_fun)
quit_btn.pack()

canvas = Canvas(windows, width=1300, height=1300, bg='lightskyblue')
canvas.pack()

circle = canvas.create_oval(100, 100, 300, 300, fill="red")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300,
                         100,
                         text='???',
                         fill="black",
                         font=('Arial', 30))
canvas.bind_all('<Key>', move_canvas)

# windows.iconbitmap("creeper.png")

img = PhotoImage(file=("creeper.png"))

my_img = canvas.create_image(500, 500, image=img)

windows.mainloop()