import pygame
import Card_File_Finder as CFF
from Deck_file import *
from Player import *

offset = 0
move_x = 0
deck = Deck()
user = Player("Bob")
points = 0


def drawACard(name):
    global points
    name.draw(deck)
    points += name.cardValue()
    return points


def imageFunction(file):
    global offset
    global move_x
    offset += 1
    move_x = 200 + 25 * offset
    image = pygame.transform.scale(pygame.image.load((file)), (75, 100))
    return image


def drawButtonPress(name):
    drawACard(name)
    file = CFF.image_finder(name)
    imageFunction(file)
