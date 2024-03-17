from ttkbootstrap import *
from tkinter import filedialog
from PIL import Image, ImageTk
import sys
import os

os.chdir(sys.path[0])


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    lable1.config(text=file_path)


def show_image():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.image = photo


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

btn1 = Button(windows, text="瀏覽", command=open_file, style="my.TButton")
btn1.grid(row=0, column=2, sticky="W")

button2 = Button(windows, text='顯示', command=show_image, style="my.TButton")
button2.grid(row=1, columnspan=3)

canvas = Canvas(windows, width=600, height=600, bg='lightskyblue')
canvas.grid(row=2, columnspan=3)

windows.mainloop()