from tkinter import *
import keyboard


def GameScreen(name):
    playing_window = Tk()
    playing_window.geometry("500x500")
    playing_window.title("BlackJack")
    label = Label(playing_window, text=f"Hello {name}")
    label.grid(column=0,row=0)
    # Quits program
    quit_button = Button(playing_window, text="Quit", command=playing_window.quit)
    quit_button.grid(row=1,column=1)
    playing_window.mainloop()