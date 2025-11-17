import pygame, random
from paddle import Paddle
from ball import Ball
from brick import Brick
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

ball_limit = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game!")


clock = pygame.time.Clock()
running = True

##################
paddle= Paddle()
balls = pygame.sprite.Group()
bricks = pygame.sprite.Group()
##################
for x in range(0, SCREEN_WIDTH, 21):
    for y in range(0, 200, 11):
        bricks.add(Brick(x, y))


while running:

    #randomly create a ball 
    if len(balls) < ball_limit:
        if random.random() > .99:
            ball = Ball()
            balls.add(ball)
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

        
    #Handle Collision
    collided_balls = pygame.sprite.spritecollide(paddle, balls, False)
    for ball in collided_balls:
        ball.y_vel = -1 * abs(ball.y_vel)

    collided_bricks = pygame.sprite.groupcollide(bricks, balls, True, False)
    
    for ball in collided_bricks.values():
        for b in ball:
            b.y_vel *= -1


    #update the screen
    paddle.update()
    balls.update()
    bricks.update()
    screen.fill(PURPLE)
    

    #Show the screen
    paddle.draw(screen)
    
    for ball in balls:
        ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
    pygame.display.flip()

    #Limits to 60FPS
    clock.tick(120)
    
