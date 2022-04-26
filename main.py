import math
import pygame
import random
pygame.init
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("circle collision")


def CircleCollision(x1,x2,y1,y2, radius):
    if (math.sqrt((x2 - x1)^2 + (y2- y1)^2))<radius:
        return True
    else:
        return False
    
    #game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game spee
while not doExit:
    chief = random.randrange(1,250)
    keef = random.randrange(1,250)
    love = random.randrange(1,250)
    sosa = random.randrange(20,100)
    xpos = random.randrange(50,750)
    ypos = random.randrange(50,750)

   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program
    #render section-----------------------------------
    pygame.draw.circle(screen, (chief,keef,love), (xpos,ypos), sosa)
    pygame.display.flip() 

    
    
    
#END GAME LOOP#######################################################
pygame.quit()    

