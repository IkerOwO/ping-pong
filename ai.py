import pygame

class AI:
    def __init__(self):
        self.rect = pygame.rect.Rect((650,200,30,150))
        self.direction = -1  # -1 es para arriba, 1 para abajo

    def ai_movement(self):
        vel = 5
        y_min, y_max = 10, 600

        self.rect.y += vel * self.direction
        if self.rect.top <= y_min:
            self.rect.top = y_min
            self.direction = 1
        if self.rect.bottom >= y_max:
            self.rect.bottom = y_max
            self.direction = -1

    def draw(self, surface):
        pygame.draw.rect(surface,(200, 85, 20), self.rect)