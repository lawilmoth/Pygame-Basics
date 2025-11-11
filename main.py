import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

#Constants 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (154, 26, 176)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game!")


clock = pygame.time.Clock()
running = True

##################
paddle= Paddle()
ball = Ball()
##################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = True
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = True

        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = False
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = False

        



    #update the screen
    paddle.update()
    ball.update()
    screen.fill(PURPLE)
    

    #Show the screen
    paddle.draw(screen)
    ball.draw(screen)
    
    pygame.display.flip()

    #Limits to 60FPS
    clock.tick(120)
