import pygame
from item import Button

class MenuWindow:
    def __init__(self, menu_window_size):
        #menu_window_size: (wdith, height)

        GREY=(200,200,200)
        self.size=menu_window_size
        self.color=GREY
        self.surface=pygame.Surface(menu_window_size)
        self.surface.fill(GREY)
        self.start_button= Button.Button("Start", (100,50) ,menu_window_size)


    def draw(self, screen ,position):
        #screen:base window
        #position: coordinate (x,y) of MenuWindow
        screen.blit(self.surface, position)
        button_position=(position[0]+(self.size[0]-self.start_button.size[0])/2, position[1]+(self.size[1]-self.start_button.size[1])/2)
        self.start_button.draw(screen, button_position)


    

