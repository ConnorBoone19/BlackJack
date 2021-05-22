import sys
import pygame
import Player
import Card_File


# for each card create a function to get the value and suit to more quickly and efficently show the image
# image = pygame.transform.scale(pygame.image.load(('PNG/2C.png')), (100, 100))


# Gets the short hand for the file assignment for the image of the specific card in the PNG folder
def suit_short_hand(suit):
    global SS
    if suit == 'Clubs':
        SS = 'C'
    elif suit == 'Spades':
        SS = 'S'
    elif suit == 'Diamonds':
        SS = 'D'
    elif suit == 'Hearts':
        SS = 'H'
    else:
        exit("Error in Card_File_Finder at suit_short_hand")
    return SS


# Gets the exact file address for the card's image
def in_folder_suit_finder(value, suit, suit_short):
    output_value = "Error in Card_File_Finder, value is not going through the if statements or skipped them"

    if value == 'Ace':
        output_value = f'PNG/{suit}/A{suit_short}.png'
        return output_value
    elif value == 'King':
        output_value = f'PNG/{suit}/K{suit_short}.png'
        return output_value
    elif value == 'Queen':
        output_value = f'PNG/{suit}/Q{suit_short}.png'
        return output_value

    elif value == 'Jack':
        output_value = f'PNG/{suit}/J{suit_short}.png'
        return output_value
    else:
        exit(f"Error with Card_File_Finder at inner if str function for {suit}")
    print(output_value)


# Finds the image of the card in the PNG folder
def image_finder(name):
    value = name.DrawnValue()
    suit = name.DrawnSuit()
    suit_short = suit_short_hand(suit)
    try:
        # Tries to convert value into an integer, if it fails that means it is a face card and does the except command
        value = int(value)
        if type(value) == int:
            output_value = f'PNG/{suit}/{value}{suit_short}.png'
            return output_value

        else:
            exit(f"Error with Card_File_Finder at inner if int function for {suit}")
    except:
        if type(value) == str:
            # print("Found String")
            if suit == 'Hearts':
                # print("Found Hearts")
                value = in_folder_suit_finder(value, suit, suit_short)
                return value
            elif suit == 'Spades':
                # print("Found Spades")
                value = in_folder_suit_finder(value, suit, suit_short)
                return value
            elif suit == 'Clubs':
                # print("Found Clubs")
                value = in_folder_suit_finder(value, suit, suit_short)
                return value
            elif suit == 'Diamonds':
                # print("Found Diamonds")
                value = in_folder_suit_finder(value, suit, suit_short)
                return value
            else:
                quit("Error with Card_File_Finder at image_finder inner function")
        else:
            quit("Error with Card_File_Finder at image_finder outer function")
