__author__ = 'Skyeyes'

import random, math, pygame
from pygame.locals import *

#main program begins
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")

#load bitmaps
space = pygame.image.load("Space.png").convert()

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if  keys[K_ESCAPE]:
        sys.exit()
    #draw backgroud
    screen.blit(space, (0,0))
    
    pygame.display.update()

