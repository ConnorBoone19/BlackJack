import pygame
import pygame_widgets
import Card_File_Finder as CFF
import New_Card_Shown
from New_Card_Shown import *
from Gui_Draw_Card import *
from Buttons_for_gui import buttonAdd
import time

offset = 0
move_x = 1
buttonPressed = 1

user = Player("Bob")
deck = Deck()
deck.shuffle()
deck.show()
drawACard(user)
pygame.init()
screen = pygame.display.set_mode((800, 600))

file = CFF.image_finder(user)


def imageFunction(file):
    global offset
    offset += 1
    image = pygame.transform.scale(pygame.image.load((file)), (75, 100))
    return image


move_x = 5
length = 1
card_image = imageFunction(file)
file = CFF.image_finder(user)


def drawButtonPress():
    global move_x
    global card_image
    global length
    drawACard(user)
    user.showHand()
    file = CFF.image_finder(user)
    card_image = imageFunction(file)
    length += 1
    move_x += 75/25



draw_button = pygame_widgets.Button(
    screen, 100, 100, 300, 150, text='Hello',
    fontSize=50, margin=20,
    inactiveColour=(255, 0, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: drawButtonPress()
)
# pgw.Button(screen, x cord, y cord, width, height)

run = True

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
    screen.fill(color='Light Green')
    for f in range(0,len(user.cards)):
        pygame.surface.Surface.blit(screen, card_image, (move_x, 450))
    draw_button.listen(events)
    draw_button.draw()

    pygame.display.update()
