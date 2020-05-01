import pygame
import random
import sys

width = 1000
height = 700
FPS = 200

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

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
        self.image.fill(green)
        self.rect = pygame.Rect(self.playerx, self.playery, 66,92)
        self.rect.center = (width/2, height/2)  

    def update(self):
        self.rect = pygame.Rect(self.playerx, self.playery, 66, 92)
  

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


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

entities = pygame.sprite.Group()

player = Player()
entities.add(player)


running = True
while running:
    clock.tick(FPS)
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running  = False
    # pressed = pygame.key.get_pressed() 
    player.moving()

    screen.fill(black)
    entities.update()
    entities.draw(screen)

    pygame.display.flip()

pygame.quit()

