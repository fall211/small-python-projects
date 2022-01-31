import tkinter as tk

window = tk.Tk()
window.title("tic tac toe")

presses = 0
status = "normal"

def press_count():
    global presses
    presses = presses + 1

def x1_change():
    if presses % 2 == 0:
        x1["text"]="x"
    else:
        x1["text"]="o"

def x2_change():
    if presses % 2 == 0:
        x2["text"]="x"
    else:
        x2["text"]="o"

def x3_change():
    if presses % 2 == 0:
        x3["text"]="x"
    else:
        x3["text"]="o"

def x4_change():
    if presses % 2 == 0:
        x4["text"]="x"
    else:
        x4["text"]="o"

def x5_change():
    if presses % 2 == 0:
        x5["text"]="x"
    else:
        x5["text"]="o"

def x6_change():
    if presses % 2 == 0:
        x6["text"]="x"
    else:
        x6["text"]="o"

def x7_change():
    if presses % 2 == 0:
        x7["text"]="x"
    else:
        x7["text"]="o"

def x8_change():
    if presses % 2 == 0:
        x8["text"]="x"
    else:
        x8["text"]="o"

def x9_change():
    if presses % 2 == 0:
        x9["text"]="x"
    else:
        x9["text"]="o"

x1 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x1_change(), press_count()]
)
x1.grid(row=0, column=0)

x2 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x2_change(), press_count()]
)
x2.grid(row=0, column=1)

x3 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x3_change(), press_count()]
)
x3.grid(row=0, column=2)

x4 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x4_change(), press_count()]
)
x4.grid(row=1, column=0)

x5 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x5_change(), press_count()]
)
x5.grid(row=1, column=1)

x6 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x6_change(), press_count()]
)
x6.grid(row=1, column=2)

x7 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x7_change(), press_count()]
)
x7.grid(row=2, column=0)

x8 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x8_change(), press_count()]
)
x8.grid(row=2, column=1)

x9 = tk.Button(
text="",
width=2,
height=2,
bg="black",
fg="white",
state = status,
command=lambda: [x9_change(), press_count()]
)
x9.grid(row=2, column=2)

def board_reset():
    global presses
    presses = 0
    x1["text"] = ""
    x2["text"] = ""
    x3["text"] = ""
    x4["text"] = ""
    x5["text"] = ""
    x6["text"] = ""
    x7["text"] = ""
    x8["text"] = ""
    x9["text"] = ""

reset_button = tk.Button(
text="reset",
width=2,
height =2,
bg="white",
fg="black",
command=board_reset,
)
reset_button.grid(row=3, column=1)



window.mainloop()
