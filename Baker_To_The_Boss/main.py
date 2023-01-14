import pygame
import os

WIDTH, HEIGHT = 800, 600 ## size of game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # ???
pygame.display.set_caption("Baker To The Boss") #name of the application

WHITE = (255, 255, 255) #constant variale for color white

FPS = 60 #set FPS
BAKER_WIDTH, BAKER_HEIGHT = 64, 64
MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT = 64, 64

BAKER_IMAGE = pygame.image.load(os.path.join('Assets', 'baker.png')) #load baker image
BAKER = pygame.transform.scale(BAKER_IMAGE, (BAKER_WIDTH, BAKER_HEIGHT)) #set scale of image

MOB_BOSS_IMAGE = pygame.image.load(os.path.join('Assets', 'mob_boss.png')) #load mob_boss image
MOB_BOSS = pygame.transform.scale(MOB_BOSS_IMAGE, (MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT))

def draw_window(baker, mob_boss):
    WIN.fill(WHITE) ##background color
    WIN.blit(BAKER, (baker.x, baker.y)) #place + position baker image
    WIN.blit(MOB_BOSS, (mob_boss.x, mob_boss.y))
    pygame.display.update() # ???

def main():
    baker = pygame.Rect(100, 300, BAKER_WIDTH, BAKER_HEIGHT) #position baker
    mob_boss = pygame.Rect(300, 100, MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT) #position mob_boss

    clock = pygame.time.Clock() # ???
    run = True
    while run:
        clock.tick(FPS) # set FPS
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                run = False

        baker.x += 1 #move baker
        draw_window(baker, mob_boss)

    pygame.quit() # if run = false, close the game

if __name__ == "__main__": # __name__ = name of file. runs the game
    main()