import sys, pygame, pygame.mixer
import os
from pygame.locals import QUIT

pygame.init()

clock = pygame.time.Clock()

size = width, height = 600, 400
white = 255,255,255
black = 0,0,0
red = 255,0,0

screen = pygame.display.set_mode(size)


screen.fill(black)

crashed = False


while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    
    mx,my = pygame.mouse.get_pos()
    screen.fill(black)
    pygame.draw.line(screen, white, [mx-5, my],[mx-5, my] 20)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit