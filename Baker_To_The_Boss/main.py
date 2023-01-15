## CODING BY ZACHARY CUERVO
## WRITING AND GAME DESIGN BY MARIO A. VANANO
## 01/14/2023
## TREASURE HACKS 3.0 2023
## ~ ~ BAKE LOTS OF CUP CAKES AND LEAVE THE WORLD A BETTER PLACE THAN YOU FOUND IT ~ ~



from re import X
import pygame
from pygame.locals import *
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

BORDER = pygame.Rect(WIDTH, HEIGHT, 10, 10) # draws a long thin rectangle... not in use right now

MAIL_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'mail_hit.mp3'))
MAIL_THROW_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'mail_throw.mp3'))

HEALTH_FONT = pygame.font.SysFont('fraktur', 32)
WINNER_FONT = pygame.font.SysFont('fraktur', 100)

FPS = 60 #set FPS

VELOCITY = 3 #set velocity

PROJECTILE_VELOCITY = 4 # set velocity for projectiles
MAX_PROJECTILE = 3 # ammo amount

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

mob_velocity = 1


vel_x = 1
vel_y = 1

def draw_window(baker, mob_boss, mail_projectiles, mob_boss_health):
    WIN.fill(WHITE) ##background color
    WIN.blit(FLOOR, (0, 0))
    
  
    mob_boss_health_text = HEALTH_FONT.render("Cupcakes Delivered: " + str(mob_boss_health), 1, WHITE)
 
    WIN.blit(mob_boss_health_text, (WIDTH - mob_boss_health_text.get_width() - 10, 10))



    WIN.blit(BAKER, (baker.x, baker.y)) #place + position baker image
    WIN.blit(MOB_BOSS, (mob_boss.x, mob_boss.y))


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



def mob_boss_directions(mob_boss, vel_x, vel_y, mob_velocity): #function for mob boss random movement

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

INTRO_TEXT_1 = ["A Cursed Family", "Chapter Three", "Baker to the Boss", "There's more to the story of our family...", "but this chapter is easier to stomach than most...", "Jameson was a baker.", "A good one, well-regarded, reasonably priced...", " ", " ", "       SPACE to continue..."]
INTRO_LINES_1 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_2 = ["There is a glass case, loaded with cakes,", " immaculately decorated. And donuts, tarts, pies.", "All presented with a keen eye and caring hand.", "On the walls are photos, Jameson with the mayor,", "Jameson standing in front of the bakery the day ", "he purchased it, Jameson and his young son, Andrew,", "Jameson with the first baked good he sold at ", "Jameson's Bakery, Andrew learning to use a whisk,", "Andrew's dog, Otis, eating an entire cake...", "       SPACE to continue..."]
INTRO_LINES_2 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_3 = ["Jameson stands behind the counter, coated in flour, ", "kneading some dough, preparing a tray of rolls.", "A ruffian, hardened and scarred, enters. He slips a set", "of conjoined, spiked, brass rings onto", "his fingers and approaches the counter.", "'Youse da bakermin?'", "'I'm a baker, yes. My name is Jameson. How can I help you?'", "'See, word dun sez youse got da bes' cakes in town. Zat true?'", "A humble man, Jameson simply smiles and responds,", "       SPACE to continue..."]
INTRO_LINES_3 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_4 = ["'I'm quite proud of my cakes, yes. I don't know about ", "the best, but I think they're quite good.'", "'My boss, see, he wants some cakes. But small-like, see'", "'Small... cakes. Bundt cakes?'", "'Smaller.'", "'Oh, I see. Pound cakes.'", "'Smaller!' The ruffian clenches his fist and raises it threateningly'", "'Hmm...'", "Ain't youse gawt some koinda cookie cuttas er sum'n'?", "       SPACE to continue..."]
INTRO_LINES_4 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_5 = ["'Yes, of course. But I think what your boss is looking", " for is something that was always meant to be small,", "not a normal cake cut into smaller cakes, right?", "'Gawtta be hand held. Sweet. It's fer his dawta's tenth", "boithday, see? Can't nuttin' mess that up or ye'll be", "sleepin' wit' da fishes. Comprondor?'", "'...Yes?'", "'Gewd. All be back in a hwhile. If ye ain't gawt", "twenty-five itty-bitty hand cakes, ye's gawta sing", "       SPACE to continue..."]
INTRO_LINES_5 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_6 = ["da happy birfday song to his datta. Ova an' ova. Once", "fer each time ya din make a cake but shoulda.", "An' if yaw don'?' He raises his fist again.", "'I'z weal deck yer head clean off aye well.'", "The ruffian with an oddly shifting accent turns", "on his heel and leaves.", "The ruffian and his boss thought they invented", "cupcakes that day, but it was really Jameson. ", "He begins feverishly theory-crafting, prototyping,", "       SPACE to continue..."]
INTRO_LINES_6 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_7 = ["and baking. Eventually, he finds his process, and using", "ramekins and pieces of parchment carefully cut into fluted circles, he", "begins the desperate task of saving his own life.", "Mercifully, when the ruffian returns, he knows it couldn't", "possibly have been enough time. Mercilessly, he", "returns with yet more instructions. Fortunately, Jameson has ", "anticipated this and prepared a batch of generic batter", "which he can flavor in many ways. Unfortunately,", "the ruffian is impatient and demanding in equal measure.", "       SPACE to continue..."]
INTRO_LINES_7 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

INTRO_TEXT_8 = ["THROW 25 CUPCAKES AT THE RUFFIAN TO WIN!", "THE RUFFIAN WILL SPEED UP AS TIME CONTINUES!", "PRESS SPACE TO THROW CUPCAKES!", "W A S D TO MOVE THE BAKER!", " ", " ", " ", " ", " ", "       SPACE to continue..."]
INTRO_LINES_8 = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]

def draw_intro_1(text, line):
    draw_text = HEALTH_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, (line+1)*50))
    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    baker = pygame.Rect(100, 300, BAKER_WIDTH, BAKER_HEIGHT) #position baker
    mob_boss = pygame.Rect(500, 100, MOB_BOSS_WIDTH, MOB_BOSS_HEIGHT) #position mob_boss

    mail_projectiles = []


    mob_velocity = 1
    random_move = 0

    mob_boss_health = 0
    

    vel_x = mob_velocity*random.randrange(-1, 1)
    vel_y = mob_velocity*random.randrange(-1, 1)



    clock = pygame.time.Clock() # ???
    run = True
    start_time = pygame.time.get_ticks()


     
    reloop = 1
    while reloop == 1:
        for i in INTRO_LINES_1:
            draw_intro_1(INTRO_TEXT_1[i], i)
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()  
            
        
    WIN.fill(BLACK)

    reloop = 1
    while reloop == 1:
        for i in INTRO_LINES_2:
            draw_intro_1(INTRO_TEXT_2[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()  

    WIN.fill(BLACK)
    reloop = 1
    while reloop == 1:

        for i in INTRO_LINES_3:
            draw_intro_1(INTRO_TEXT_3[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2

        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()  
    WIN.fill(BLACK)
    reloop = 1
    while reloop == 1:

        for i in INTRO_LINES_4:
            draw_intro_1(INTRO_TEXT_4[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()  

    WIN.fill(BLACK)
    reloop = 1
    while reloop == 1:

        for i in INTRO_LINES_5:
            draw_intro_1(INTRO_TEXT_5[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()  

    WIN.fill(BLACK)
    reloop = 1
    while reloop == 1:

        for i in INTRO_LINES_6:
            draw_intro_1(INTRO_TEXT_6[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()   

    WIN.fill(BLACK)
    reloop = 1
    while reloop == 1:

        for i in INTRO_LINES_7:
            draw_intro_1(INTRO_TEXT_7[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2
        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()   

    WIN.fill(BLACK)
    reloop = 1
    while reloop == 1:

        for i in INTRO_LINES_8:
            draw_intro_1(INTRO_TEXT_8[i], i)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reloop = 2

        for event in pygame.event.get(): # check for close game
            if event.type == pygame.QUIT: #if click windows X close button
                pygame.quit()   

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
                if event.key == pygame.K_SPACE and len(mail_projectiles) < MAX_PROJECTILE: # when K is pressed AND less than number of projectile on screen
                    mail_bullet = pygame.Rect(baker.x + baker.width, baker.y + baker.height//2, 10, 5) ## creates projectile rectangle
                    mail_projectiles.append(mail_bullet)
                    MAIL_THROW_SOUND.play()



            if event.type == MOB_BOSS_HIT:
                mob_boss_health += 1
                MAIL_HIT_SOUND.play()



        if mob_boss_health > 25:
            winner_text = "Baker Wins!"

            if winner_text != "":
                draw_winner(winner_text)
                break



        keys_pressed = pygame.key.get_pressed() #checks which keys are pressed
        baker_handle_movement(keys_pressed, baker)
        mob_boss_directions(mob_boss, vel_x, vel_y, mob_velocity)


        handle_projectiles(mail_projectiles, baker, mob_boss)

        draw_window(baker, mob_boss, mail_projectiles, mob_boss_health)

    pygame.quit() # if run = false, close the game

if __name__ == "__main__": # __name__ = name of file. runs the game
    main()