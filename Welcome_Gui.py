from tkinter import *

def welcomeScreen():
    gui = Tk()
    gui.title("TextBox Input")
    gui.geometry('400x200')
    gui.configure(background="light green")
    gui.wm_attributes('-transparent')

    def Input():
        name = input_text.get(1.0, "end-1c")
        user_name.config(text="Welcome: " + name)
        user_name.pack()
        startButton.pack()
        return name

    def startGame():
        return 

    welcome = Label(gui, text="Welcome to my game!")
    welcome.pack()

    welcome2 = Label(gui, text="Please enter your name below and click continue")
    welcome2.pack()

    input_text = Text(gui, height=5, width=20)
    input_text.pack()

    printButton = Button(gui, text="Print", command=Input)
    printButton.pack()


    user_name = Label(gui, text="")

    startButton = Button(gui,text="Start", command = startGame())
    gui.mainloop()


welcomeScreen()
