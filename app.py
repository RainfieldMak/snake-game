import pygame
from pygame.math import Vector2
from item import  Items




def main():
    
    SCREEN_SIZE = (800, 800)
    FPS = 60
    WHITE = (255, 255, 255)
    MOVEMENT_SPEED= 10
    MENU_SIZE=(300,300)

    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()



    running = True
 
    main_=Items.Main(screen, SCREEN_SIZE,MOVEMENT_SPEED,  MENU_SIZE)


    SCREEN_UPDATE=pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while running:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SCREEN_UPDATE:

                if  main_.get_pause()== False:
                   
                   #player lose
                   if  main_.update() == False:
                        
                        #pause game and reset
                        main_.set_pause(True)
                        main_.reset()
                         
                

            #Keyboard arrow input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and main_.snake.get_direction().y !=  MOVEMENT_SPEED :
                    main_.snake.set_direction(Vector2(0,MOVEMENT_SPEED*-1))

                if event.key == pygame.K_DOWN and main_.snake.get_direction().y !=  (MOVEMENT_SPEED *-1) :
                    main_.snake.set_direction(Vector2(0,MOVEMENT_SPEED))
                
                if event.key == pygame.K_LEFT and main_.snake.get_direction().x !=  MOVEMENT_SPEED :
                    main_.snake.set_direction(Vector2(MOVEMENT_SPEED*-1,0))

                if event.key == pygame.K_RIGHT and main_.snake.get_direction().x !=  (MOVEMENT_SPEED *-1) :
                    main_.snake.set_direction(Vector2(MOVEMENT_SPEED,0))
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_.menu.start_button.onlick():
                    main_.start()
                


        screen.fill(WHITE)    
        main_.draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
