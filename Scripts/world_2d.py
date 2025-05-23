import pygame
import sys

def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cube2D")
    clock = pygame.time.Clock()
    player = pygame.Rect(100, 100, 50, 50)
    speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: player.y -= speed
        if keys[pygame.K_s]: player.y += speed
        if keys[pygame.K_a]: player.x -= speed
        if keys[pygame.K_d]: player.x += speed

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
