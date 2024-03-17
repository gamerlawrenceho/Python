from ttkbootstrap import *
from tkinter import filedialog
from PIL import Image, ImageTk
import sys
import os


def test():
    entry_text = entry.get()
    try:
        ans = eval(entry_text)
    except:
        ans = 'Error'
    lable1.config(text=ans)


os.chdir(sys.path[0])

windows = tk.Tk()

windows.title("Lawrence")

windows.option_add("*font", ("Helvetica", 20))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))

entry = Entry(windows, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

btn1 = Button(windows, text="顯示計算結果", command=test, style="my.TButton")
btn1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

lable1 = Label(windows, text='計算結果')
lable1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

windows.mainloop()