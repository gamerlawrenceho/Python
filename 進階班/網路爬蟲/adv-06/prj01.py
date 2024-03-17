from ttkbootstrap import *
from PIL import Image, ImageTk
import sys
import os

os.chdir(sys.path[0])


def on_switch_change():
    check_label.config(text=str(check_type.get()))


windows = tk.Tk()
windows.title("Lawrence")
windows.option_add("*font", ("Helvetica", 20))
style = Style(theme='cyborg')
style.configure('TButton', font=('Helvetica', 20))
check_type = BooleanVar()
check_type.set(True)

check_label = Label(windows, text="True")
check_label.grid(row=1, column=2)

check = Checkbutton(windows,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=1, column=1)
windows.mainloop()