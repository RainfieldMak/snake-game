import pygame
from pygame.math import Vector2


class Button:

    def __init__(self, text ,size, menu_w ):
        self.text=text
        self.size= size
        self.font_size= 15
        self.font=pygame.font.Font(None, self.font_size)
        self.button_rect=None
        
       
        

    def draw(self, screen, position):
        Black=(0,0,0)
        WHITE=(255,255,255)
        
        #draw button
        rect=pygame.Rect(position[0],position[1],self.size[0],self.size[1])
        self.button_rect=rect
        pygame.draw.rect(screen,WHITE, rect )

        #place text on button
        text_surface= self.font.render(self.text, True, Black )
        text_rect = text_surface.get_rect()
        text_rect.center = (position[0]+self.size[0] // 2,position[1]+self.size[1] // 2)
      
        screen.blit(text_surface, text_rect)


    #problem, can still clickl after button disapperam, need to add extra if statement
    def onlick(self):
       
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            mouse_pos=pygame.mouse.get_pos()
            if self.button_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                return True


                        


      

