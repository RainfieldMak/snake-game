import pygame
from pygame.math import Vector2
import random
import os 

class Apple:
    def __init__(self,SCREEN, SCREEN_SIZE):
        DEFAULT_SIZE = (20, 20)
        self.default_size = DEFAULT_SIZE
        self.position_x = random.randint(1, SCREEN_SIZE[0]-self.default_size[0])
        self.position_y = random.randint(1, SCREEN_SIZE[1]-self.default_size[1])
        self.vector = Vector2(self.position_x, self.position_y)
        self.screen=SCREEN
        self.screen_size = SCREEN_SIZE
        self.image = self.load_apple_image()
        self.rect= pygame.Rect(self.get_x(),self.get_y(), self.default_size[0],self.default_size[1])
        

    def get_x(self):
        return self.position_x
    
    def get_y(self):
        return self.position_y
    
    def get_rect(self):
        return self.rect
    
    def set_rect(self, rect):
        self.rect=rect



    def draw_apple(self):
        self.screen.blit(self.image, (self.vector[0],self.vector[1]))

    

    def get_vector(self):
        return self.vector
    

    
    #change to pre-load and save to another environment to reduce time for loading ?
    def load_apple_image(self):

        current_file = __file__
        parent_directory = os.path.dirname(current_file)
        file_path = os.path.join(parent_directory, "..", "assets", "apple.jpg")

   
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, self.default_size)
        return image