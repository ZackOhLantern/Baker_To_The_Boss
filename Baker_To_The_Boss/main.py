import pygame
import os

WIDTH, HEIGHT = 800, 600 ## size of game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # ???
pygame.display.set_caption("Baker To The Boss") #name of the application

WHITE = (255, 255, 255) #constant variale for color white

FPS = 60 #set FPS

BAKER_IMAGE = pygame.image.load(os.path.join('Assets', 'baker.png')) #load baker image
MOB_BOSS_IMAGE = pygame.image.load(os.path.join('Assets', 'mob_boss.png')) #load mob_boss image

def draw_window():
    WIN.fill(WHITE) ##background color
    WIN.blit(BAKER_IMAGE, (300, 100)) #place + position baker image
    pygame.display.update() # ???

def main():
    clock = pygame.time.Clock() # ???
    run = True
    while run:
        clock.tick(FPS) # set FPS
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()