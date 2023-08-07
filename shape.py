from tkinter import END, Tk, Canvas
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror 
from time import sleep
def error(text):
    showerror("Shape", str(text))
win = Tk()
win.resizable(0, 0)
win.title("Shape")
canvas = Canvas(height=1000, width=1000, borderwidth=2, border=2)
canvas.config(background="black")
def arc(x1, y1, x2, y2, fill, outline):
    try:
        canvas.create_arc(x1, y1, x2, y2, fill=fill, outline=outline)
    except Exception as e:
        error(e)
def rect(x1, y1, x2, y2, fill, outline):
    try:
        canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)
    except Exception as e:
        error(e)
def line(x1, y1, x2, y2, fill):
    try:
        canvas.create_arc(x1, y1, x2, y2, fill=fill)
    except Exception as e:
        error(e)
def oval(x1, y1, x2, y2, fill, outline):
    try:
        canvas.create_oval(x1, y1, x2, y2, fill=fill, outline=outline)
    except Exception as e:
        error(e)
def text(x1, y1, fill, text):
    try:
        canvas.create_text(x1, y1, fill=fill, text=text)
    except Exception as e:
        error(e)
def execute(code=str):
    canvas.delete("all")
    for i in code.split("\n"):
        command = i.split(" ")
        match command[0]:
            case "arc":
                arc(int(command[1]), int(command[2]), int(command[3]), int(command[4]), command[5], command[6])
            case "rect":
                rect(int(command[1]), int(command[2]), int(command[3]), int(command[4]), command[5], command[6])
            case "line":
                line(int(command[1]), int(command[2]), int(command[3]), int(command[4]), command[5])
            case "oval":
                oval(int(command[1]), int(command[2]), int(command[3]), int(command[4]), command[5], command[6])
            case "text":
                text(int(command[1]), int(command[2]), command[3], " ".join(command[4:]))
            case "clear":
                canvas.delete("all")
            case "wait":
                sleep(float(command[1]))
            case "":
                pass
            case _:
                error("Unknown command: " + command[0])
        canvas.update()
code = ScrolledText(width=100, height=61)
code.grid(column=1, row=0)
run = Button(text="Execute", command=lambda: execute(code.get("1.0", END)[:-1]), width=135)
run.grid(column=1, row=1)
canvas.grid(column=0, row=0, rowspan=2)
win.mainloop()