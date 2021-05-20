import pygame_widgets as Button


def buttonAdd(window,x_cord,y_cord,width,height,text_option,default_color,active_color,
              edge_radius,command):
    action = Button.Button(
        window, x_cord, y_cord, width, height, text=text_option,
        inactiveColour=default_color,
        pressedColour=active_color, radius=edge_radius,
        onClick=lambda: command)
    return action