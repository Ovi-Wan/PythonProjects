from tkinter import *

def button_click(num):
    global calcul
    calcul = calcul + str(num)
    calcul_label.set(calcul)

def egal():
    global calcul
    try:
        total = str(eval(calcul))
        calcul_label.set(total)
        calcul = total
    except ZeroDivisionError:
        calcul_label.set("Eroare")
        calcul = ""
    except SyntaxError:
        calcul_label.set("Introdu un număr!")
        calcul = ""

def clear():
    global calcul
    calcul_label.set("0")
    calcul = ""

def procentaj1():
    global calcul
    try:
        total = float(eval(calcul)) / 100
        calcul = str(total)
        calcul_label.set(calcul)
    except:
        calcul_label.set("Eroare")
        calcul = ""

def backspace1():
    global calcul
    if calcul:
        calcul = calcul[:-1]
        calcul_label.set(calcul if calcul else "0")


fer = Tk()
fer.title("Calculator iOS Style")
fer.geometry("320x400")
fer.configure(bg="#F1F2F6")

calcul = ""
calcul_label = StringVar()
calcul_label.set("0")


bara = Label(fer, textvariable=calcul_label, font=("San Francisco", 24), bg="white", fg="black", anchor="e", padx=10, height=2)
bara.pack(fill="both")


rama = Frame(fer, bg="#F1F2F6")
rama.pack(pady=10)


button_style = {
    "font": ("San Francisco", 18),
    "bg": "#E0E0E0",
    "fg": "black",
    "relief": "flat",
    "width": 4,
    "height": 2
}
button_special_style = {
    **button_style,
    "bg": "#FF9500",
    "fg": "white"
}


buttons = [
    ("%", lambda: procentaj1()), ("C", clear), ("B", backspace1), ("/", lambda: button_click("/")),
    ("7", lambda: button_click(7)), ("8", lambda: button_click(8)), ("9", lambda: button_click(9)), ("X", lambda: button_click("*")),
    ("4", lambda: button_click(4)), ("5", lambda: button_click(5)), ("6", lambda: button_click(6)), ("-", lambda: button_click("-")),
    ("1", lambda: button_click(1)), ("2", lambda: button_click(2)), ("3", lambda: button_click(3)), ("+", lambda: button_click("+")),
    ("0", lambda: button_click(0)), (".", lambda: button_click(".")), ("=", egal),
]


row = 0
col = 0
for text, command in buttons:
    if text == "=":
        Button(rama, text=text, command=command, **button_special_style).grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        col += 1
    else:
        Button(rama, text=text, command=command, **button_style).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(5):
    rama.rowconfigure(i, weight=1)
for j in range(4):
    rama.columnconfigure(j, weight=1)

fer.mainloop()
