from re import X
import pygame
import os
import datetime
import random

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600 ## size of game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # ???
pygame.display.set_caption("Baker To The Boss") #name of the application

WHITE = (255, 255, 255) #constant variable for color white
BLACK = (0, 0 ,0) #constant variable for color black
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH, 0, 10, HEIGHT) # draws a long thin rectangle... not in use right now

MAIL_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'mail_hit.mp3'))
MAIL_THROW_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'mail_throw.mp3'))

HEALTH_FONT = pygame.font.SysFont('fraktur', 40)
WINNER_FONT = pygame.font.SysFont('fraktur', 100)

FPS = 60 #set FPS

VELOCITY = 3 #set velocity
##MOB_BOSS_VELOCITY = 1
PROJECTILE_VELOCITY = 4 # set velocity for projectiles
MAX_PROJECTILE = 25 # ammo amount

BAKER_WIDTH, BAKER_HEIGHT = 64, 64
MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT = 64, 64

BAKER_HIT = pygame.USEREVENT + 1 ## events have to have different '+number'
MOB_BOSS_HIT = pygame.USEREVENT + 2 

BAKER_IMAGE = pygame.image.load(os.path.join('Assets', 'baker.png')) #load baker image
BAKER = pygame.transform.scale(BAKER_IMAGE, (BAKER_WIDTH, BAKER_HEIGHT)) #set scale of image

MAIL_IMAGE = pygame.image.load(os.path.join('Assets', 'mail_projectile.png')) #load mail img
MAIL_PROJECTILE = pygame.transform.scale(MAIL_IMAGE, (BAKER_WIDTH, BAKER_HEIGHT)) #set scale of image


MOB_BOSS_IMAGE = pygame.image.load(os.path.join('Assets', 'mob_boss.png')) #load mob_boss image
MOB_BOSS = pygame.transform.scale(MOB_BOSS_IMAGE, (MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT))

FLOOR = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'brick_wall_tile.png')), (WIDTH, HEIGHT))
#global MOB_BOSS_VELOCITY

#MOB_BOSS_VELOCITY = 1
#global vel_x
#global vel_y
mob_velocity = 1

#vel_x = mob_velocity*random.randrange(-1, 1, 1)
#vel_y = mob_velocity*random.randrange(-1, 1, 1)
vel_x = 1
vel_y = 1

def draw_window(baker, mob_boss, mail_projectiles, mob_boss_health):
    WIN.fill(WHITE) ##background color
    WIN.blit(FLOOR, (0, 0))
    
    ##baker_health_text = HEALTH_FONT.render("Health: " + str(baker_health), 1, WHITE)
    mob_boss_health_text = HEALTH_FONT.render("Cupcakes Delivered: " + str(mob_boss_health), 1, WHITE)
    ##WIN.blit(baker_health_text, (10, 10))
    WIN.blit(mob_boss_health_text, (WIDTH - mob_boss_health_text.get_width() - 10, 10))

    # pygame.draw.rect(WIN, BLACK, BORDER) // not in use right now
    WIN.blit(BAKER, (baker.x, baker.y)) #place + position baker image
    WIN.blit(MOB_BOSS, (mob_boss.x, mob_boss.y))
    ## WIN.blit(MAIL_PROJECTILE, (0, 0))

    for mail_bullet in mail_projectiles:
        pygame.draw.rect(WIN, RED, mail_bullet)

    pygame.display.update() # ???

def baker_handle_movement(keys_pressed, baker): #function for baker movement
    if keys_pressed[pygame.K_w] and baker.y - VELOCITY > 0: #W key pressed / UP and boundary limit
        baker.y -= VELOCITY
    if keys_pressed[pygame.K_a] and baker.x - VELOCITY > 0: #A key pressed / LEFT and boundary limit
        baker.x -= VELOCITY
    if keys_pressed[pygame.K_s] and baker.y + VELOCITY < HEIGHT: #S key pressed / DOWN and boundary limit
        baker.y += VELOCITY
    if keys_pressed[pygame.K_d] and baker.x + VELOCITY < WIDTH: #D key pressed / RIGHT and boundary limit
        baker.x += VELOCITY

#def mob_boss_handle_movement(mob_boss): #function for mob boss movement
#        mob_boss.x += vel_x
 #       mob_boss.y += vel_y

def mob_boss_directions(mob_boss, vel_x, vel_y, mob_velocity): #function for mob boss random movement
    #mob_boss.x += vel_x
    #mob_boss.y += vel_y
    #if random_move == 1:
       # mob_velocity += 1  
       # vel_x = random.randrange(-1, 1, 1)
      #  vel_y = random.randrange(-1, 1, 1)
        mob_boss.x += (mob_velocity * vel_x)
        mob_boss.y += (mob_velocity * vel_y)
        if mob_boss.x < -1:
            mob_boss.x = WIDTH
        if mob_boss.x > WIDTH:
            mob_boss.x = 0
        if mob_boss.y > HEIGHT:
            mob_boss.y = 0
        if mob_boss.y < 0:
            mob_boss.y = HEIGHT



def handle_projectiles(mail_projectiles, baker, mob_boss): #projectile function
    for mail_bullet in mail_projectiles:
        mail_bullet.x += PROJECTILE_VELOCITY
        if baker.colliderect(mail_bullet):
            pygame.event.post(pygame.event.Event(BAKER_HIT))
            mail_projectiles.remove(mail_bullet)

    for mail_bullet in mail_projectiles:
        mail_bullet.x += PROJECTILE_VELOCITY
        if mob_boss.colliderect(mail_bullet):
            pygame.event.post(pygame.event.Event(MOB_BOSS_HIT))
            mail_projectiles.remove(mail_bullet)
        elif mail_bullet.x > WIDTH:
            mail_projectiles.remove(mail_bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    baker = pygame.Rect(100, 300, BAKER_WIDTH, BAKER_HEIGHT) #position baker
    mob_boss = pygame.Rect(500, 100, MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT) #position mob_boss

    mail_projectiles = []

    ##baker_health = 10
    #vel_x = random.randrange(-1, 1, 1)
    #vel_y = random.randrange(-1, 1, 1)
    mob_velocity = 1
    random_move = 0

    mob_boss_health = 0
    
    #mob_velocity = 1
    vel_x = mob_velocity*random.randrange(-1, 1)
    vel_y = mob_velocity*random.randrange(-1, 1)

    #vel_x = 1
    #vel_y = 1


    clock = pygame.time.Clock() # ???
    run = True
    start_time = pygame.time.get_ticks()

    while run:
        clock.tick(FPS) # set FPS
        random_move = 0

        timer = pygame.time.get_ticks()  ## reset timer 2 seconds
        if (pygame.time.get_ticks() - start_time) > 2000:
            print(pygame.time.get_ticks() - start_time)
            start_time = pygame.time.get_ticks()
            random_move = 1
            mob_velocity += 1  
            vel_x = random.randrange(-1, 2)
            vel_y = random.randrange(-1, 2)
            while (vel_x == 0) & (vel_y == 0):
                vel_x = random.randrange(-1, 2)
                vel_y = random.randrange(-1, 2)
            print(vel_x)
            print(vel_y)


       

        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                run = False

            if event.type == pygame.KEYDOWN: # creating projectile system
                if event.key == pygame.K_k and len(mail_projectiles) < MAX_PROJECTILE: # when K is pressed AND less than number of projectile on screen
                    mail_bullet = pygame.Rect(baker.x + baker.width, baker.y + baker.height//2, 10, 5) ## creates projectile rectangle
                    mail_projectiles.append(mail_bullet)
                    MAIL_THROW_SOUND.play()

            ##if event.type == BAKER_HIT:
                ##baker_health -= 1
                ##MAIL_HIT_SOUND.play()

            if event.type == MOB_BOSS_HIT:
                mob_boss_health += 1
                MAIL_HIT_SOUND.play()

        #mob_boss.x += vel_x
        #mob_boss.y += vel_y

        ##winner_text = ""
        ##if baker_health <= 0:
            ##winner_text = "Mob Boss Wins!"

        if mob_boss_health > 25:
            winner_text = "Baker Wins!"

            if winner_text != "":
                draw_winner(winner_text)
                break



        keys_pressed = pygame.key.get_pressed() #checks which keys are pressed
        baker_handle_movement(keys_pressed, baker)
        mob_boss_directions(mob_boss, vel_x, vel_y, mob_velocity)
        #mob_boss_handle_movement(mob_boss)

        handle_projectiles(mail_projectiles, baker, mob_boss)

        draw_window(baker, mob_boss, mail_projectiles, mob_boss_health)

    pygame.quit() # if run = false, close the game

if __name__ == "__main__": # __name__ = name of file. runs the game
    main()