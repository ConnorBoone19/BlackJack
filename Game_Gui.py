from tkinter import *
from PIL import Image, ImageTk
from Gui_Draw_Card import *
from Welcome_Gui import welcomeScreen

game_over = False
x_shift = 0
thing = []
def gameStartScreen(name):

    user = Player(name)
    deck = Deck()
    deck.shuffle()


    def drawCard():
        global game_over
        # if the game is over then stop
        if not game_over:
            user.draw(deck)
            CardImage(root)
            if user.points > 21:
                game_over = True
                newGameButton.place(x=50, y=250)
        else:
            return


    def reset():
        global game_over
        global x_shift
        global thing
        deck.resetDeck()
        user.resetPlayer()
        game_over = False
        root.destroy()
        welcomeScreen()

        print(user.cards)


    class CardImage(Frame):

        def __init__(self, master=None):
            global x_shift
            Frame.__init__(self, master)
            self.master = master
            load = Image.open(self.GetFile())
            load = load.resize((100, 125))
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.place(x=50 + x_shift, y=50)
            x_shift += 25

        def GetFile(self):
            image_file_location = CFF.image_finder(user)
            return image_file_location


    # Create Tkinter Object
    root = Tk()
    root.geometry("500x500")
    root.configure(background='Light green')
    drawButton = Button(root, text="Draw", fg='black', bg='red', command=lambda: drawCard(), height=1, width=5)
    drawButton.place(x=400, y=400)

    newGameButton = Button(root, text="New Game?", fg='black', bg='red', command=lambda: reset(), height=1, width=10)

    # Execute Tkinter
    root.mainloop()
