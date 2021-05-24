from tkinter import *
from Game_Gui import gameStartScreen

name = ""


def welcomeScreen():
    gui = Tk()
    gui.title("TextBox Input")
    gui.geometry('500x300')
    gui.configure(background="light green")
    gui.wm_attributes('-transparent')

    def Input():
        # Gets users name
        global name
        name = input_text.get(1.0, "end-1c")
        user_name.config(text="Welcome: " + name)
        user_name.pack()
        startButton.pack()
        return name

    def startGame():
        # Checks to see if user has inputed their name
        if not name == "":
            gui.destroy()
            gameStartScreen(name)
            return
        else:
            exit()

    welcome = Label(gui, text="Welcome to my game!")
    welcome.pack()

    welcome2 = Label(gui, text="Please enter your name below and click continue")
    welcome2.pack()
    welcome3 = Label(gui, text="after you are done drawing please click stand and the dealer will draw! \n at this "
                               "point in time there is no way to repeat the game so if you would like \n to play again"
                               "please press quit and re-open the 'main.py' file")
    welcome3.pack()
    input_text = Text(gui, height=5, width=20)
    input_text.pack()

    printButton = Button(gui, text="Print", command=Input)
    printButton.pack()

    user_name = Label(gui, text="")

    startButton = Button(gui, text="Start", command=lambda: startGame())
    gui.mainloop()


