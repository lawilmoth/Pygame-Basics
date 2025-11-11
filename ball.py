import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        """All of this code happens when we create the paddle"""
        super().__init__()
        self.radius = 20
        self.color = "#fa00af"
        self.speed = 10
        

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        
        pygame.draw.circle(self.image, self.color, (400, 300), self.radius)

        self.rect = self.image.get_rect()

        self.rect.center = (400, 300)

        self.moving_right = False
        self.moving_left = False

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if self.moving_right and self.rect.right < 800:
            self.rect.x += self.speed 