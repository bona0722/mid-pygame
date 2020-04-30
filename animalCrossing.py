import pygame
import sys
import time
import random
import pygame as pg
from pygame.locals import *


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)

FPS = 60


pg.init()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Animal Crossing")
clock = pg.time.Clock()

screen = pg.image.load('island.png')
screen = pg.transform.scale(screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    
