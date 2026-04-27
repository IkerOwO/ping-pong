import pygame
import player
import ai

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,620))
Player = player.Player()
AI = ai.AI()

# Funcion para actualizar la pantalla
def update_screen():
    pygame.display.update()

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Color del background
        screen.fill("black")
        AI.draw(screen)
        AI.ai_movement()
        Player.draw(screen)
        Player.handle_keys()
        update_screen()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()