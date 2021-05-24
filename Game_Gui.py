from tkinter import *
from PIL import Image, ImageTk
from Gui_Draw_Card import *
from Dealer_file import *
from time import *

# placeholders
x_shift_dealer = 0
x_shift_user = 0
user_win = False
dealer_win = False
game_over = False


def gameStartScreen(name):
    user = Player(name)
    dealer = Dealer("dealer")
    deck = Deck()
    deck.shuffle()

    def dealerHit():
        global game_over
        # dealer draws until it cannot
        while dealer.canDraw:
            dealer.draw(deck)
            CardImageDealer()
        # check to make sure dealer cannot draw anymore
        if dealer.canDraw == True:
            exit("error when dealer draw, dealer did not draw until it could not")
        game_over = True
        isThereWinner()

    def whoWon():
        if dealer_win == True or user_win == True:
            if dealer_win:
                winner = "dealer"
                return winner
            elif user_win:
                winner = "dealer"
                return winner
            else:
                winner = "neither of you"
                return winner
        else:
            if dealer.points > 21:
                winner = "you"
                return winner
            elif user.points > 21:
                winner = "dealer"
                return winner
            elif dealer.points > user.points:
                winner = "dealer"
                return winner
            elif user.points > dealer.points:
                winner = "dealer"
                return winner
            else:
                exit("Error with who won, possibly dealerHit file")


    def isThereWinner():
        global game_over
        global user_win
        global dealer_win
        # checks to see if game is over
        if not game_over:
            # checks to see if the scores of either dealer or user are at or above 21
            if user.points > 21:
                dealer_win = True
                game_over = True
            elif dealer.points > 21:
                user_win = True
                game_over = True
            elif user.points == 21:
                user_win = True
                game_over = True
            elif dealer.points == 21:
                dealer_win = True
                game_over = True
        if game_over:
            # if game is over then let user know with text
            game_text = Label(
                text=f"The dealer had a combined score of {dealer.points}, \n while you had a combined score of {user.points}, \n this means that {whoWon()} won!")
            game_text.place(x=150, y=200)

    def drawCard():
        # checks to see if there is a winner or not and determines if user can draw a card
        isThereWinner()
        if not game_over:
            user.draw(deck)
            CardImageUser()
            # rechecks if there is a winner to lock user from drawing
            isThereWinner()
        else:
            return

    def quit():
        # self explanatory
        root.quit()

    def start():
        # on the press of start button, the draw and stand buttons are created while the start button is deleted
        # dealer draws first two cards
        for i in range(0,2):
            dealer.draw(deck)
            CardImageDealer()
        drawButton.place(x=400, y=400)
        standButton.place(x=400, y=450)
        startButton.destroy()

    class CardImageDealer(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.imageLoad()

        def imageLoad(self):
            global x_shift_dealer
            load = Image.open(self.getFile())
            load = load.resize((100, 125))
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.place(x=50 + x_shift_dealer, y=50)
            x_shift_dealer += 50
            if len(dealer.cards) == 1:
                load = Image.open("PNG/Misc/red_back.png")
                load = load.resize((75, 125))
                render = ImageTk.PhotoImage(load)
                fake = Label(image=render)
                fake.image = render
                fake.place(x=50, y=50)

        def getFile(self):
            image_file_location = CFF.image_finder(dealer)
            return image_file_location


    class CardImageUser(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.imageLoad()

        def imageLoad(self):
            global x_shift_user
            # loads image from get file command
            load = Image.open(self.getFile())
            load = load.resize((100, 125))
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)

            img.image = render
            img.place(x=50 + x_shift_user, y=300)
            x_shift_user += 50

        def getFile(self):
            # gets the location of the file within the folder using Card_File_Finder.py
            image_file_location = CFF.image_finder(user)
            return image_file_location

    # Create Tkinter window
    root = Tk()
    root.geometry("500x500")
    root.configure(background='Light green')
    startButton = Button(root, text="Start", fg='black', bg='red', command=lambda: start(), height=1, width=5)
    startButton.place(x=400, y=400)

    drawButton = Button(root, text="Draw", fg='black', bg='red', command=lambda: drawCard(), height=1, width=5)

    standButton = Button(root, text="Stand", fg="black", bg="red", command=lambda: dealerHit(), height=1, width=5)

    quitButton = Button(root, text="Quit", fg='black', bg='red', command=lambda: quit(), height=1, width=10)
    quitButton.place(x=50, y=250)

    root.mainloop()



