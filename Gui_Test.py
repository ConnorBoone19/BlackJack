import pygame
from pygame_widgets import Button
pygame.init()
win = pygame.display.set_mode((600, 600))
def buttonPress():
    print("hi")
button = Button(
            win, 100, 100, 300, 150, text='Hello',
            fontSize=50, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=20,
            onClick=lambda: buttonPress()
         )

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    button.listen(events)
    button.draw()

    pygame.display.update()
