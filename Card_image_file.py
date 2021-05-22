from New_Card_Shown import *
from Player import *
import Card_File_Finder as CFF


class image_class:
    def __init__(self, user,screen):
        self.screen = screen
        self.offset = 0
        self.user = user
        self.user_card = drawACard(self.user)
        self.file = CFF.image_finder(self.user)

        return

    def drawButtonPress(self,user):
        print("hello here")
        the_image = pygame.surface.Surface.blit(self.screen, self.imageFunction(), (self.offset(), 450))
        return the_image

    def imageFunction(self):
        card_file_image = pygame.transform.scale(pygame.image.load(self.file), (75, 100))
        return card_file_image

    def offset(self):
        self.offset += 1
        x_offset = 50 + (self.offset * 25)
        return x_offset
