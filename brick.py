import pygame

class Brick(pygame.sprite.Sprite):
    ORANGE = (227, 93, 20)
    
    def __init__(self, x, y):
        """All of this code happens when we create the paddle"""
        super().__init__()
        self.width = 20
        self.height = 10
        self.color = (self.ORANGE)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    
    def update(self):
        pass