import pygame

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((100,200,30,150))

    def handle_keys(self):
         key = pygame.key.get_pressed()
         y_min, y_max = 10, 600
         if key[pygame.K_LEFT]:
            self.rect.move_ip(-10, 0)
         if key[pygame.K_RIGHT]:
            self.rect.move_ip(10, 0)
         if key[pygame.K_UP]:
            self.rect.move_ip(0, -10)
         if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 10)

         # Limitar el movimiento vertical
         if self.rect.top < y_min:
            self.rect.top = y_min
         if self.rect.bottom > y_max:
            self.rect.bottom = y_max

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)
   