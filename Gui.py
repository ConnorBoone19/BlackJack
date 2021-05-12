from tkinter import *
import keyboard

if __name__ == '__main__':

    gui = Tk()
    gui.geometry("250x250")
    # Quits program
    Button(gui, text="Quit", command=gui.quit).pack()
    gui.mainloop()