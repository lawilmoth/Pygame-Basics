import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """All of this code happens when we create the paddle"""
        super().__init__()
        self.radius = 10
        self.color = "#fa00af"
        self.x_vel = random.randint(-10, 10)
        self.y_vel = random.randint(-10, 10)
        self.x = random.randint(100, 700)

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        pygame.draw.circle(self.image, self.color, (400, 300), self.radius)

        self.rect = self.image.get_rect()

        self.rect.center = (400, 300)



    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    
    def update(self):

        if self.rect.right >= 800 or self.rect.left <= 0:
            #Change direction
            self.x_vel *= -1
            
        if self.rect.bottom >= 600 or self.rect.top <= 0:
            #Change direction
            self.y_vel *= -1

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        