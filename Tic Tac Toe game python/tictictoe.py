import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x700+0+0")
root.title("Tic Toc Toe")
root.configure(background='#99ff99')

Tops = Frame(root, bg='#00ffff', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Advance Tic Toc Toe Game",
                 bd=21, bg='#99ff99', fg='#ff9933', justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg='#66ff33', bd=10,
                  width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500,
                  padx=10, pady=2, bg='#6600ff', relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500,
                   padx=10, pady=2, bg='#6600ff', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200,
                    padx=10, pady=2, bg='#6600ff', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200,
                    padx=10, pady=2, bg='#6600ff', relief=RIDGE)
RightFrame2.grid(row=1, column=0)


PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True


def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] == "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] == "O"
        click = True
        scorekeeper()


def scorekeeper():
    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")

    if(button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won a game")


def reset():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "

    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")


def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


lblPlayerX = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player X :", padx=2, pady=2,
                   bg='#99ff99')
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=2, fg="black",
                   textvariable=PlayerX, width=14, justify=LEFT).grid(row=0, column=1)

lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player O :", padx=2, pady=2,
                   bg='#99ff99')
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=2, fg="black",
                   textvariable=PlayerO, width=14, justify=LEFT).grid(row=1, column=1)


btnReset = Button(RightFrame2, text="Reset", font=('Times 26 bold'),
                  height=1, width=31, bg='gainsboro', command=reset)
btnReset.grid(row=0, column=0, padx=6, pady=30)

btnNewGame = Button(RightFrame2, text="New Game", font=('Times 26 bold'),
                    height=1, width=31, bg='gainsboro', command=NewGame)
btnNewGame.grid(row=1, column=0, padx=6, pady=30)


button1 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro', command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro')
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro')
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro')
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro')
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro')
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(LeftFrame, text="", font=('Times 26 bold'),
                 height=3, width=8, bg='gainsboro')
button9.grid(row=3, column=2, sticky=S+N+E+W)


root.mainloop()

