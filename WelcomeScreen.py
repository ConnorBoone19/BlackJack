from tkinter import *
from PlayingScreen import GameScreen
name = ""


def get_name():
    name = name_field.get("1.0", "end")
    print(name)
    welcome_screen.destroy()
    GameScreen(name)

if __name__ == '__main__':
    welcome_screen = Tk()
    welcome_screen.configure(background = "Light blue")
    welcome_screen.title("BlackJack")
    welcome_screen.geometry("250x250")

    greeting = Label(welcome_screen, text="Welcome to my BlackJack Game")
    greeting.grid(column=0, row=1)

    name_ask = Label(welcome_screen, text="What is your name?")
    name_ask.grid(column=0, row=2)

    # Asks user for their name
    name_field = Text(welcome_screen, height = 5, width = 25)
    name_field.grid(column=0, row=3)
    # gets users name
    next_button = Button(welcome_screen, text="Start", command=get_name)
    next_button.grid(column=0, row=10)

    welcome_screen.mainloop()
