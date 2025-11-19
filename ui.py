import pygame
class UI:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)

    def draw_score(self, screen, score):
        score_surf = self.font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))

    def draw_lives(self, screen, lives):
        for i in range(lives):
            pygame.draw.circle(screen, "#fa00af", (750 - (i * 30), 30), 10)