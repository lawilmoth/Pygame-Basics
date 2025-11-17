import pygame

class Paddle(pygame.sprite.Sprite):
    GREEN = (0, 255, 0)
    

    def __init__(self):
        """All of this code happens when we create the paddle"""
        super().__init__()
        self.width = 200
        self.height = 20
        self.speed = 10
        self.color = (self.GREEN)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()

        self.rect.center = (400, 575)

        self.moving_right = False
        self.moving_left = False

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if self.moving_right and self.rect.right < 800:
            self.rect.x += self.speed 