import tkinter as tk
import random

def brown():
    root.config(bg="brown")
def red():
    root.config(bg="red")
def blue():
    root.config(bg="blue")
def green():
    root.config(bg="green")
def yellow():
    root.config(bg="yellow")
def purple():
    root.config(bg="purple")
def orange():
    root.config(bg="orange")
def colors():
    colors = [red,blue,green,purple,yellow,orange,brown]
    random.choice(colors)()

def brown2():
    label.config(bg="brown")
def red2():
    label.config(bg="red")
def blue2():
    label.config(bg="blue")
def green2():
    label.config(bg="green")
def yellow2():
    label.config(bg="yellow")
def purple2():
    label.config(bg="purple")
def orange2():
    label.config(bg="orange")
def colors2():
    colors2 = [red2,blue2,green2,purple2,yellow2,orange2,brown2]
    random.choice(colors2)()

def brown3():
    label.config(fg="brown")
def red3():
    label.config(fg="red")
def blue3():
    label.config(fg="blue")
def green3():
    label.config(fg="green")
def yellow3():
    label.config(fg="yellow")
def purple3():
    label.config(fg="purple")
def orange3():
    label.config(fg="orange")
def colors3():
    colors3 = [red3,blue3,green3,purple3,yellow3,orange3,brown3]
    random.choice(colors3)()


def text():
    text = entry.get()
    label2 = tk.Label(root, text=text, font=("Arial", 15), bg="lightblue", fg="grey")
    label2.pack()

root = tk.Tk()
root.title("sandbox")
root.geometry("600x600")

label = tk.Label(root, text="Напиши будь-що:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Тицьни сюди, щоб побачити що ти написав", command=text)
button.pack()

button2 = tk.Button(root, text="  Вихід  ", command=root.quit)
button2.place(x=375, y=15)

menubar = tk.Menu(root)
color_menu = tk.Menu(menubar, tearoff=1)
color_menu.add_command(label="Змінити колір фону", command=colors)
color_menu.add_command(label="Змінити колір тексту", command=colors3)
color_menu.add_command(label="Змінити колір фону тексту", command=colors2)
menubar.add_cascade(label="Вибір кольору", menu=color_menu)
root.config(menu=menubar)

root.mainloop()