import tkinter as tk
from tkinter import *
import math

win = tk.Tk()
win.geometry("700x500")

rAnswer = StringVar()
rAnswer.set("")


def mathFunction():
    import math

    a1 = e1.get()
    h1 = e2.get()
    c1 = e3.get()
    b1 = e4.get()

    if h1 == "":
        s = (int(a1) + int(b1) + int(c1)) / 2
        answer = round(math.sqrt(s * (s - int(a1)) *
                                 (s - int(b1)) * (s - int(c1))), 1)
    elif float(h1) > 0:
        answer = round(((int(b1) * int(h1)) / 2), 1)

    rAnswer.set("This is the area of the triangle: " + str(answer))


image1 = PhotoImage(file="triangle.png")
l1 = Label(win, image=image1)
l2 = Label(win, text="Enter in as much information about the")
l3 = Label(win, text="triangle shown and I will calculate the area")
l4 = Label(win, textvariable=rAnswer, font=(None, 10))
e1 = Entry(win, text="a", width=7)
e2 = Entry(win, text="height", width=7)
e3 = Entry(win, text="c", width=7)
e4 = Entry(win, text="b", width=7)
b1 = Button(win, text="Calculate", width=10, command=mathFunction)


l1.place(x=50, y=0)
l2.place(x=100, y=305)
l3.place(x=95, y=325)
l4.place(x=435, y=310)
e1.place(x=225, y=100)
e2.place(x=350, y=100)
e3.place(x=425, y=100)
e4.place(x=300, y=225)
b1.place(x=350, y=310)

win.mainloop()
