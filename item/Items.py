from item import Snake, Apple
class Main:

    def __init__(self, screen, SCREEN_SIZE,MOVEMENT_SPEED) :
        self.apple=Apple.Apple(screen, SCREEN_SIZE)
        self.snake = Snake.Snake(screen, SCREEN_SIZE,MOVEMENT_SPEED)
        self.screen=screen
        self.screen_size= SCREEN_SIZE
        self.movement_speed=MOVEMENT_SPEED


    def get_screen(self):
        return self.screen
    
    def get_screen_size(self):
        return self.screen_size
    

    def update(self):
        
        self.snake.move()
        head=self.snake.get_head()

        #collide with apple, generate new apple and extend snake
        if self.check_collision():
            self.snake.extend()
            self.get_new_apple()
        

    def check_collision(self):
        if self.snake.get_head().colliderect(self.apple.get_rect()):
            return True


    def get_new_apple(self):
        self.apple= Apple.Apple(self.get_screen(),self.get_screen_size())
        self.apple.draw_apple()


    def draw(self):
        self.apple.draw_apple()
        self.snake.draw_snake()
