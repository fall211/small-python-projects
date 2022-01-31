import random
import tkinter as tk


window = tk.Tk()
window.title("RPS")

def textfield():
    global textF
    textF = tk.Entry(
    bg="black",
    fg="white",
    justify="center",
)
    textF.pack()


def rps():
    x = textF.get()
    print("you said " + x)
    list = ["rock", "paper", "scissors"]
    output = random.choice(list)
    print("i picked " + output)

    if x == output:
            print("tie")
            result = "tie"
    elif x == "rock":
        if output == "scissors":
            print("you win")
            result = "you win"
        else:
            print("you lose")
            result = "you lose"

    elif x == "paper":
        if output == "rock":
            print("you win")
            result = "you win"
        else:
            print("you lose")
            result = "you lose"

    elif x == "scissors":
        if output == "paper":
            print("you win")
            result = "you win"
        else:
            print("you lose")
            result = "you lose"

    else:
        print("cant play with " + x)
        print("please type either rock paper or scissors")
        result = "invalid entry"

    resultbox = tk.Label(
    text=result,
    )
    resultbox.pack()


def enterbutton():
    contB = tk.Button(
    text="enter",
    width=4,
    height=2,
    bg="black",
    fg="white",
    command=rps,
)
    contB.pack()

button = tk.Button(
    text="Rock Paper Scissors, Click to Play",
    width=15,
    height=5,
    bg="black",
    fg="white",
    wraplength=150,
    command=lambda: [textfield(), enterbutton()],
)
button.pack()


window.mainloop()
