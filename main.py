import pygame
import player
import ai

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,620))
white = (255,255,255)
Player = player.Player()
AI = ai.AI()

# Pelota
ball_x = 370
ball_y = 200
ball_radius = 15
ball_vel_x = 5
ball_vel_y = 5

# Funcion para actualizar la pantalla
def update_screen():
    pygame.display.update()

def move_ball():
    global ball_x, ball_y, ball_vel_x, ball_vel_y
    # Actualizamos la posicion
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Creamos rectángulo que rodea la pelota para las colisiones
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    # Colisión con bordes superior/inferior
    if ball_rect.top <= 0 or ball_rect.bottom >= 620:
        ball_vel_y *= -1

    # Si la pelota sale, vuelve a la posicion inicial
    if ball_rect.right >= 800 or ball_rect.left <= 0:
        ball_x = 370
        ball_y = 200

    # Colisión con los jugadores
    if ball_rect.colliderect(Player.rect) or ball_rect.colliderect(AI.rect):
        ball_vel_x *= -1

    # Dibujamos la pelota
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Color del background
        screen.fill("black")

        AI.draw(screen)
        AI.ai_movement(ball_y)
        Player.draw(screen)
        Player.handle_keys()
        move_ball()
        update_screen()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()