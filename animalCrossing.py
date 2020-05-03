import pygame
import sys
import os
from setting import *
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption("Animal Crossing")
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock() #< #화면을 초 당 몇 번 출력하는지. 게임의 fps설정 가능

screen_width = 700
screen_height = 400

class Entity(pygame.sprite.Sprite) : #sprite init
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.image = pygame.Surface((50,50))
        self.playerx= (screen_width/2) #rect 좌표
        self.playery= (screen_height/2)
        self.rect.center = (screen_width/2, screen_height/2)

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        self.rect = pygame.Rect(self.playerx, self.playery, 50,50)
        if 0< self.playerx < screen_width and 0<self.playery<screen_height:
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

all_sprites_list = pygame.sprite.Group()
class button(): #버튼 구현 button(image, x축, y축) 
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        
    def draw(self): #draw()
        screen.blit(self.image, (self.x,self.y))

    def isOver(self, pos): #mouse가 버튼 내 좌표에 있으면 True반환. boundary(pygame.mouse.get_pos()
        width = self.image.get_width()
        height = self.image.get_height()

        if pos[0] < self.x + width and pos[0] > self.x:
            if pos[1] < self.y + height and pos[1] > self.y:
                return True
        return False


#시작 메뉴 스크린 버튼
start_b = button(start_icon, 500, 550)
guide_b = button(guide_icon, 650, 550)
exit_b = button(exit_icon, 800, 550)
#설명스크린 버튼
exitG_b = button(exitG_icon, 500,50)
keepG_b = button(keepG_icon,400, 50)

# portF #낚시 포탈
# portS #
# portE #

        #portB =  pygame.Rect(start_icon, white, 66, 92) #곤충 포탈 실험
def start():
    if start_sc == True:
        screen.blit(start_bg, (-200,0))
        start_b.draw()
        guide_b.draw()
        exit_b.draw()
        pygame.display.update()

def guide():
    if guide_sc == True:
        screen.fill(white)
        # screen.blit(start_bg, (-200,0))  #< guide_bg 이미지 구하면 이미지에 맞춰 x축 y축 추가해주기
        exitG_b.draw()
        keepG_b.draw()
        pygame.display.update()

def gameMap():
    global all_sprites_list
    
    if gameMap_sc == True: 
        screen.blit(img_scale, (0, 0))
        screen.blit(img_scale_sea, (0, 0))
        screen.blit(img_scale_mos, (500, 500))
        player = Player()
        all_sprites_list.add(player)
        all_sprites_list.update()
        pygame.display.update()

# def fish(self):
#     if fish_sc == True:
# def fishG(self):
#     if fishG_sc == True:
# def bugHunt(self):
#     if bugHunt_sc == True:
# def bugG(self): # 벌레잡기 설명
#     if bugG_sc == True:
# def store(self):
#     if store_sc == True:
# def storeG(self):
#     if storeG_sc == True:
# def home(self):
#     if home_sc == True:
# def homeG(self):
#     if homeG_sc == True:

def main(): #게임을 실행할 때 게임에서 발생한 event에 대한 설정이나 사용자의 게임 알고리즘이 여기서 작성돼야함
    clock.tick(100)
    global start_sc
    global guide_sc
    global gameMap_sc
    player = Player()
    while True:

        # start()
        # guide()
        # gameMap()
        # fish()
        # fishG()
        # bugHunt()
        # bugG()
        # store()
        # storeG()
        # home()
        # homeG()

        for event in pygame.event.get(): #게임중에 무슨 이벤트인지 for문으로 검사.
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: #마우스로 버튼 클릭시 이벤트
                if start_b.isOver(pos):
                    start_sc = False
                    gameMap_sc = True

                    screen.fill(black)

                elif guide_b.isOver(pos):
                    start_sc = False
                    guide_sc = True
                    screen.fill(black)

                elif exit_b.isOver(pos):
                    pygame.quit()
                    sys.exit()


        pygame.display.flip()

if __name__ == '__main__':
    main()