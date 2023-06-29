import pygame
from pygame.math import Vector2


class Snake():

    def __init__(self,SCREEN, SCREEN_SIZE,MOVEMENT_SPEED):
        self.body= [Vector2(400,400),Vector2(401,400),Vector2(402,400)]
        self.screen=SCREEN
        self.screen_size= SCREEN_SIZE
        self.direction=Vector2(MOVEMENT_SPEED,0)
        self.block_size=(20,20)
        self.head= pygame.Rect(400,400, self.block_size[0],self.block_size[1])


    def get_direction(self):
        return self.direction

    def set_direction(self,direction):
        self.direction=direction


    def get_body(self):
        return self.body
    
    def set_body(self,body):
        self.body=body


    def set_head(self, rect):
        self.head=rect
    
    def get_head(self):
        return self.head

    def draw_snake(self):
        for part in self.body:
            rect= pygame.Rect(part.x,part.y, self.block_size[0],self.block_size[1])
            BLUE= (0,0,255)
            pygame.draw.rect(self.screen,BLUE,rect)

    def move(self):
        
        #create a copy
        body_new= self.get_body()
        body_new=body_new[0:-1]
        head=pygame.Rect(self.body[0].x+self.get_direction().x, self.body[0].y,self.block_size[0],self.block_size[1] )
        
        #set current head position
        self.set_head(head)
        body_new.insert(0,self.body[0]+self.get_direction())
        self.set_body( body_new)


    def extend(self):
        body_copy=self.get_body()
        body_copy.insert(0,self.body[0]+self.get_direction())
        self.set_body(body_copy)

        