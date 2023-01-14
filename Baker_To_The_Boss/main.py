import pygame
import os

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baker To The Boss")

WHITE = (255, 255, 255)

FPS = 60

BAKER_IMAGE = pygame.image.load(os.path.join('Assets', 'baker.png'))
MOB_BOSS_IMAGE = pygame.image.load(os.path.join('Assets', 'mob_boss.png'))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BAKER_IMAGE, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()