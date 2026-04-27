import pygame

class AI:
    def __init__(self):
        self.rect = pygame.rect.Rect((650,200,30,150))
        self.direction = -1  # -1 es para arriba, 1 para abajo

    def ai_movement(self, ball_y):
        vel = 5
        y_min, y_max = 10, 600

        # Movemos la "IA" hacia la pelota
        if self.rect.centery < ball_y:
            self.rect.y += vel
        elif self.rect.centery > ball_y:
            self.rect.y -= vel

        # Limitamos el movimiento vertical
        if self.rect.top < y_min:
            self.rect.top = y_min
        if self.rect.bottom > y_max:
            self.rect.bottom = y_max

    def draw(self, surface):
        pygame.draw.rect(surface,(200, 85, 20), self.rect)