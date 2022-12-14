from tkinter.ttk import Label, Button, Entry
from tkinter import Tk, StringVar

WIDTH = 250
HEIGHT = 180


def popup(string):
    root = Tk()
    width = int(WIDTH / 2)
    height = int(HEIGHT / 2)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int(screen_width / 2 - (WIDTH+width) / 2)
    y = int(screen_height / 2 - (HEIGHT+height) / 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.resizable(False, False)

    root.title("answer")
    Label(root, text=string).pack()
    root.mainloop()


def string_set(string, num1, num2):
    string.set("{}<select operator below>{}".format(num1.get(), num2.get()))


def add(num1, num2):
    popup(int(num1.get()) + int(num2.get()))


def subtract(num1, num2):
    popup(int(num1.get()) - int(num2.get()))


def multiply(num1, num2):
    popup(int(num1.get()) * int(num2.get()))


def divide(num1, num2):
    popup(int(num1.get()) / int(num2.get()))


def test(*args):
    print(args)



root = Tk()
root.title("Operator Selector")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - WIDTH / 2)
center_y = int(screen_height / 2 - HEIGHT / 2)
root.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')
root.resizable(False, False)

num1 = StringVar()
num2 = StringVar()
num1.set("5")
num2.set("8")
string = StringVar()
string_set(string, num1, num2)
num1.trace('w', lambda s, x, y: string_set(string, num1, num2))
num2.trace('w', lambda s, x, y: string_set(string, num1, num2))

Entry(root, textvariable=num1).pack()
Entry(root, textvariable=num2).pack()
Label(root, textvariable=string).pack()
Button(root, text="+", command=lambda: add(num1, num2)).pack()
Button(root, text="-", command=lambda: subtract(num1, num2)).pack()
Button(root, text="*", command=lambda: multiply(num1, num2)).pack()
Button(root, text="/", command=lambda: divide(num1, num2)).pack()
root.mainloop()
