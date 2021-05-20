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
deck = Deck()
deck.shuffle()
user = Player("Bob")

drawACard(user)
pygame.init()
screen = pygame.display.set_mode((800, 600))

file = CFF.image_finder(user)


def imageFunction(file):
    global offset
    global move_x
    offset += 1
    move_x = 200 + 25 * offset
    image = pygame.transform.scale(pygame.image.load((file)), (75, 100))
    return image


card_image = imageFunction(file)


def drawButtonPress():
    global buttonPressed
    buttonPressed += 1


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
    for c in range(len(user.cards)):
        file = CFF.image_finder(user)
        card_image = imageFunction(file)
        pygame.surface.Surface.blit(screen, card_image, (move_x, 450))
    draw_button.listen(events)
    draw_button.draw()

    pygame.display.update()
