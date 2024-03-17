from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def test():
    print("test")


windows = tk.Tk()

windows.title("Lawrence")

windows.option_add("*font", ("Helvetica", 20))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))

lable = Label(windows, text='選擇檔案:')
lable.grid(row=0, column=0, sticky='E')

lable1 = Label(windows, text='無')
lable1.grid(row=0, column=1, sticky='E')

btn1 = Button(windows, text="瀏覽", command=test, style="TButton")
btn1.grid(row=0, column=2, sticky="W")

button2 = Button(windows, text='顯示', command=test, style="my.TButton")
button2.grid(row=1, columnspan=3)

canvas = Canvas(windows, width=1300, height=1300, bg='lightskyblue')
canvas.grid(row=2, columnspan=3)

windows.mainloop()