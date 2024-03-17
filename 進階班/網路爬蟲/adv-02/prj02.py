from tkinter import *
import sys
import os

os.chdir(sys.path[0])


def move_object(event, object, dx, dy):
    canvas.move(object, dx, dy)


def exit_fun():
    windows.destroy()


windows = Tk()
windows.title("My First GUI")

quit_btn = Button(windows, text="Quit", command=exit_fun)
quit_btn.pack()

canvas = Canvas(windows, width=1300, height=1300, bg='lightskyblue')
canvas.pack()

circle = canvas.create_oval(100, 100, 300, 300, fill="red")
msg = canvas.create_text(300,
                         100,
                         text='???',
                         fill="black",
                         font=('Arial', 30))

canvas.bind_all('<Right>', lambda event: move_object(event, circle, 10, 0))
canvas.bind_all('<Left>', lambda event: move_object(event, circle, -10, 0))
canvas.bind_all('<Up>', lambda event: move_object(event, circle, 0, -10))
canvas.bind_all('<Down>', lambda event: move_object(event, circle, 0, 10))
canvas.bind_all('<d>', lambda event: move_object(event, rect, 10, 0))
canvas.bind_all('<a>', lambda event: move_object(event, rect, -10, 0))
canvas.bind_all('<w>', lambda event: move_object(event, rect, 0, -10))
canvas.bind_all('<s>', lambda event: move_object(event, rect, 0, 10))

# windows.iconbitmap("creeper.png")

img = PhotoImage(file=("creeper.png"))

my_img = canvas.create_image(500, 500, image=img)

rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
windows.mainloop()