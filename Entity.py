import pygame
import random
import sys
import math
from setting import *
import os
import time
from time import sleep


class Entity(pygame.sprite.Sprite) : 
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)

class Player(Entity) :
    #sprite for the Player
    def __init__(self) :
        Entity.__init__(self)
        self.image = pygame.Surface((50,50))
        self.playerx= width/2
        self.playery= height/2 
        self.image.fill(green) #플레이어 이미지 필요 
        self.rect = pygame.Rect(self.playerx, self.playery, 50,50)
        self.rect.center = (width/2, height/2)  

    def update(self):
        self.rect = pygame.Rect(self.playerx, self.playery, 50, 50)
  

    def moving(self): #걷는 함수, 방향키 > 걷는다. ctrl + 방향키를 누르면 뛸 수 있다.
        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]: 
            self.playerx -= 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_LEFT]:
            self.playerx -= 2
        if key_event[pygame.K_RIGHT]:
            self.playerx += 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_RIGHT]:
            self.playerx += 2
        if key_event[pygame.K_UP]:
            self.playery -= 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_UP]:
            self.playery -= 2
        if key_event[pygame.K_DOWN]:
            self.playery += 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_DOWN]:
            self.playery += 2


class Enemy(Entity) :
    def __init__(self) :
        Entity.__init__(self)
        mos = pygame.image.load('image/mos.png')
        img_scale_mos = pygame.transform.scale(mos,(30,30))
        self.image = img_scale_mos
        self.rect = self.image.get_rect()

    def pos(self) :
        self.rect.x = random.randint(0, width)
        self.rect.y = random.randint(0, height)
        
    def update(self) :
        self.rect.y += 4
        self.rect.x += 4
        if self.rect.y >= height or self.rect.x >= width :
            self.pos()


# #initialize pygame and create window
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Bug Game")
# clock = pygame.time.Clock()

# entities = pygame.sprite.Group()

# player = Player()
# enemy = Enemy(400, 500)
# entities.add(player)
# entities.add(enemy)


# running = True
# while running:
#     clock.tick(FPS)
#     # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             running  = False
#     # pressed = pygame.key.get_pressed() 
#     player.moving()
#     # enemy.ranmove()
#     # enemy.move()
#     screen.fill(black)
#     entities.update()
#     entities.draw(screen)

#     pygame.display.flip()

# pygame.quit()



