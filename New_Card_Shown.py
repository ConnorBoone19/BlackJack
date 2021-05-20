from Gui_Draw_Card import *


class CardDrawnShow:
    def __init__(self,name,window):
        self.card_image = imageFunction(self.file)
        self.user = name
        self.offset = 0
        self.move_x = 0
        self.file = 0
        self.points = 0
        self.window = window
        return

    def drawACard(self):
        self.user.draw(deck)
        self.points += self.user.cardValue()
        return self.points

    def imageFunction(self):
        self.offset += 1
        self.move_x = 200 + 25 * self.offset
        image = pygame.transform.scale(pygame.image.load(self.file), (75, 100))
        return image

    def drawButtonPress(self):
        drawACard(self.user)
        self.file = CFF.image_finder(self.user)
        pygame.surface.Surface.blit(self.window, self.card_image, (move_x, 450))
