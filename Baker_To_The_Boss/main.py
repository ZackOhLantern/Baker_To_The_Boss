import pygame
import os

WIDTH, HEIGHT = 800, 600 ## size of game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # ???
pygame.display.set_caption("Baker To The Boss") #name of the application

WHITE = (255, 255, 255) #constant variable for color white
BLACK = (0, 0 ,0) #constant variable for color black

BORDER = pygame.Rect(WIDTH, 0, 10, HEIGHT) # draws a long thin rectangle... not in use right now

FPS = 60 #set FPS
VELOCITY = 5 #set velocity
BAKER_WIDTH, BAKER_HEIGHT = 64, 64
MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT = 64, 64

BAKER_IMAGE = pygame.image.load(os.path.join('Assets', 'baker.png')) #load baker image
BAKER = pygame.transform.scale(BAKER_IMAGE, (BAKER_WIDTH, BAKER_HEIGHT)) #set scale of image

MOB_BOSS_IMAGE = pygame.image.load(os.path.join('Assets', 'mob_boss.png')) #load mob_boss image
MOB_BOSS = pygame.transform.scale(MOB_BOSS_IMAGE, (MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT))

def draw_window(baker, mob_boss):
    WIN.fill(WHITE) ##background color
    # pygame.draw.rect(WIN, BLACK, BORDER) // not in use right now
    WIN.blit(BAKER, (baker.x, baker.y)) #place + position baker image
    WIN.blit(MOB_BOSS, (mob_boss.x, mob_boss.y))
    pygame.display.update() # ???

def baker_handle_movement(keys_pressed, baker): #function for baker movement
    if keys_pressed[pygame.K_w] and baker.y - VELOCITY > 0: #W key pressed / UP
        baker.y -= VELOCITY
    if keys_pressed[pygame.K_a] and baker.x - VELOCITY > 0: #A key pressed / LEFT
        baker.x -= VELOCITY
    if keys_pressed[pygame.K_s] and baker.y + VELOCITY < HEIGHT: #S key pressed / DOWN
        baker.y += VELOCITY
    if keys_pressed[pygame.K_d] and baker.x + VELOCITY < WIDTH: #D key pressed / RIGHT
        baker.x += VELOCITY

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


        keys_pressed = pygame.key.get_pressed() #checks which keys are pressed
        baker_handle_movement(keys_pressed, baker)


        draw_window(baker, mob_boss)

    pygame.quit() # if run = false, close the game

if __name__ == "__main__": # __name__ = name of file. runs the game
    main()