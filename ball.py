import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """All of this code happens when we create the paddle"""
        super().__init__()
        self.radius = 15
        self.color = "#fa00af"
        self.x_vel = random.randint(-5, 5)
        self.y_vel = random.randint(-5, -1)
        self.x = random.randint(100, 700)

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        pygame.draw.circle(self.image, self.color, (400, 300), self.radius)

        self.rect = self.image.get_rect()

        self.rect.center = (400, 300)

        self.is_playing = False


    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    
    def update(self, paddle):
        if self.is_playing:
            if self.rect.right >= 800 or self.rect.left <= 0:
                #Change direction
                self.x_vel *= -1
                
            if self.rect.top <= 0:
                #Change direction
                self.y_vel = abs(self.y_vel)

            if self.rect.top > 600:
                self.kill()

            self.rect.x += self.x_vel
            self.rect.y += self.y_vel

        else:
            self.rect.center = (
                paddle.rect.centerx, 
                paddle.rect.top - self.radius)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.is_playing = True
