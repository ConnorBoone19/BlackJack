from tkinter import *
from PIL import Image, ImageTk
from Gui_Draw_Card import *
from Dealer_file import *

i = 1
first_card = ""
game_over = False
x_shift = 0
x_shift_dealer = 0
start = True
one_more = True
hidden_card = ""


def gameStartScreen(name):
    user = Player(name)
    dealer = Dealer("dealer")
    deck = Deck()
    deck.shuffle()

    def canDealerDraw():
        global one_more
        dealer_points = dealer.points
        if dealer_points == 21:
            result = "Win"
            return result
        elif dealer_points > 21:
            result = "Lose"
            gameOver()
            return result
        elif dealer_points >= 17:
            result = False
            one_more = True
            return result
        elif dealer_points <= 17:
            result = True
            return result
        else:
            exit("Error at canDealerDraw")

    def drawCard():
        global game_over
        gameOver()
        # if the game is over then stop
        if not game_over:
            user.draw(deck)
            CardImageUser(root)
            if user.points > 21:
                game_over = True
                gameOver()
        else:
            return

    def reset():
        exit()

    def gameOver():
        global game_over
        if dealer.points >= 17 or user.points >= 21:
            game_over = True
        if game_over:

            game_text = Label(
                text=f"The dealer had a combined score of {dealer.points} \n while you had a combined score of {user.points},\n this means that {whoWon()} won!")
            game_text.place(x=150, y=200)
        else:
            return

    def whoWon():
        if dealer.points > 21 or user.points > 21:
            if dealer.points > 21:
                winner = "you"
                return winner
            elif user.points > 21:
                winner = "dealer"
                return winner
        elif user.points < dealer.points:
            winner = "the Dealer"
            return winner
        elif dealer.points < user.points <= 21:
            winner = "You"
            return winner
        else:
            winner = "you tied so neither of you"
            return winner

    def stand():
        global game_over
        global i
        if i == 1:
            drawButton.destroy()
            i = 0
        if not game_over:
            dealer.draw(deck)
            CardImageDealer()
        else:
            gameOver()

    def start():
        global start

        dealer.draw(deck)
        CardImageDealer()
        dealer.draw(deck)
        CardImageDealer()
        drawButton.place(x=400, y=400)
        standButton.place(x=400, y=450)
        startButton.destroy()
        start = False

    class CardImageDealer(Frame):
        def __init__(self, master=None):
            global hidden_card
            global x_shift_dealer
            global game_over
            Frame.__init__(self, master)
            self.master = master
            if not dealer.points >= 17:
                load = Image.open(self.GetFile())
                load = load.resize((75, 125))
                render = ImageTk.PhotoImage(load)
                img = Label(image=render)
                img.image = render
                img.place(x=50 + x_shift_dealer, y=50)
                x_shift_dealer += 75
                if len(dealer.cards) == 1:
                    load = Image.open("PNG/Misc/red_back.png")
                    load = load.resize((75, 125))
                    render = ImageTk.PhotoImage(load)
                    hidden_card = Label(image=render)
                    hidden_card.image = render
                    hidden_card.place(x=50, y=50)
            else:
                game_over = True
            if game_over:
                hidden_card.destroy()

        def GetFile(self):
            image_file_location = CFF.image_finder(dealer)
            return image_file_location

    class CardImageUser(Frame):
        def __init__(self, master=None):
            global x_shift
            Frame.__init__(self, master)
            self.master = master
            load = Image.open(self.GetFile())
            load = load.resize((75, 125))
            render = ImageTk.PhotoImage(load)
            img = Label(image=render)
            img.image = render
            img.place(x=50 + x_shift, y=300)
            x_shift += 75

        def GetFile(self):
            image_file_location = CFF.image_finder(user)
            return image_file_location

    # Create Tkinter Object
    root = Tk()
    root.geometry("500x500")
    root.configure(background='Light green')
    startButton = Button(root, text="Start", fg='black', bg='red', command=lambda: start(), height=1, width=5)
    startButton.place(x=400, y=400)

    drawButton = Button(root, text="Draw", fg='black', bg='red', command=lambda: drawCard(), height=1, width=5)

    standButton = Button(root, text="Stand", fg="black", bg="red", command=lambda: stand(), height=1, width=5)

    quitButton = Button(root, text="Quit", fg='black', bg='red', command=lambda: reset(), height=1, width=10)
    quitButton.place(x=50, y=250)

    root.mainloop()


gameStartScreen("connor")
