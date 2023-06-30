from item import Score, Snake, Apple,Menu,Score
class Main:

    def __init__(self, screen, SCREEN_SIZE,MOVEMENT_SPEED, MENU_SIZE) :
        self.apple=Apple.Apple(screen, SCREEN_SIZE)
        self.snake = Snake.Snake(screen, SCREEN_SIZE,MOVEMENT_SPEED)
        self.menu= Menu.MenuWindow((300,300))
        self.screen=screen
        self.screen_size= SCREEN_SIZE
        self.movement_speed=MOVEMENT_SPEED
        self.menu_size= MENU_SIZE
        self.pause= True
        self.score=Score.Score()
       



    def set_pause(self,flag):
        self.pause=flag

    def get_pause(self):
        return self.pause

    def get_screen(self):
        return self.screen
    
    def get_screen_size(self):
        return self.screen_size
    
    def get_movement_speed(self):
        return self.movement_speed
    

    def update(self):

    
        self.snake.move()
        if self.game_over():
            return False
            
        else:
            head=self.snake.get_head()

            #collide with apple, generate new apple and extend snake
            if self.check_collision():
                self.snake.extend()
                self.get_new_apple()
                self.score.update_score()
            return True
           
        

    def check_collision(self):
        if self.snake.get_head().colliderect(self.apple.get_rect()):
            return True


    def get_new_apple(self):
        self.apple= Apple.Apple(self.get_screen(),self.get_screen_size())
        self.apple.draw_apple()


    def draw(self):
        
        
        self.apple.draw_apple()
        self.snake.draw_snake()
        menu_position = ((self.screen_size[0]- self.menu_size[0])/2,(self.screen_size[1]-self.menu_size[1])/2 )
        if self.get_pause():
            self.menu.draw(self.screen, menu_position)

        else:
            self.score.draw(self.screen)
            


    def game_over(self):
        head=self.snake.get_body()[0]
        screen_size=self.get_screen_size()
        if head.x >0 and head.x <screen_size[0] and head.y > 0 and head.y < screen_size[1]:
            return False
        else:
            return True


    def start(self):
        self.set_pause(False)
        print (self.pause)
        

    def reset(self):
        self.apple=Apple.Apple(self.get_screen(), self.get_screen_size())
        self.snake = Snake.Snake(self.get_screen(), self.get_screen_size(),self.get_movement_speed())
        self.score.reset() 
    