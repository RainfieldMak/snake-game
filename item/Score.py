import pygame


class Score:

    def __init__(self):
        self.text="0"
        self.size=(150,150)
        self.position=(750,0)
        self.font_size=50
        self.font=pygame.font.Font(None, self.font_size)
        self.alpha= 128

    

    def set_text(self, score):
        self.text= score

    def get_text(self):
        return self.text

    def draw(self,screen):
        RED= (255,0,0)
        text_surface= self.font.render(self.text, True, RED)
        text_surface.set_alpha(self.alpha)
        text_rect=text_surface.get_rect()
        screen.blit(text_surface,self.position)




    def update_score(self):
        cur=int(self.get_text())
        cur+=1
        self.set_text(str(cur))
        

    def reset(self):
        self.text="0"