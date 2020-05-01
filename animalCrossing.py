import pygame, sys, os
import insertSc #event
from pygame.locals import QUIT

pygame.init() #초기화를 해줘야함.
pygame.display.set_caption("Animal Crossing") #게임 제목을 써줌. 화면이 꺼지기 전까지 제목이 계속 유지되므로 전역변수로 설정하기
width, height = 1000, 700
screen = pygame.display.set_mode((width, height)) #x축,y축 생성
 # 화면을 초기화하거나 화면에 데이터 추가하는 변수
clock = pygame.time.Clock() #< #화면을 초 당 몇 번 출력하는지. 게임의 fps설정 가능

#color
saddleBrown = (139, 69, 19) #button color
white = (255, 255, 255)
black = (0, 0, 0)

#image
start_bg = pygame.image.load(os.path.join("image", "start_background.jpg")).convert()
bg = pygame.image.load('image/island.png')
house = pygame.image.load('image/House.png')
market = pygame.image.load('image/market.png')
fishzone = pygame.image.load('image/fishzone.png')
mos = pygame.image.load('image/mos.png')
img_scale = pygame.transform.scale(bg, (width, height)) #크기변환
img_scale_house = pygame.transform.scale(house, (150, 150))
img_scale_market = pygame.transform.scale(market,(150,150))
img_scale_fishzone = pygame.transform.scale(fishzone,(150,150))
img_scale_mos = pygame.transform.scale(mos,(150,150))

#icon image
start_icon = pygame.image.load('image/start_icon.png') #start버튼
guide_icon = pygame.image.load('image/guide_icon.png') #guide버튼
exit_icon = pygame.image.load('image/exit_icon.png') #exit버튼

#screen
start_sc = True #첫화면
gameMap_sc = False #게임 전체 맵
guide_sc = False #설명서
fish_sc = False #낚시맵 fishing
fishG_sc = False #낚시 설명 fishing Guide
bugHunt_sc = False #곤충맵 bug hunting
bugG_sc = False #곤충잡기 설명 bug hunting Guide
store_sc = False #상점맵
storeG_sc = False #물건 구입 설명
home_sc = False #집맵
homeG_sc = False #집꾸미기 설명 home Interior Guide

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



def main(): #게임을 실행할 때 게임에서 발생한 event에 대한 설정이나 사용자의 게임 알고리즘이 여기서 작성돼야함
    clock.tick(100)
    while True: 

        for event in pygame.event.get(): #게임중에 무슨 이벤트인지 for문으로 검사.
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                if exit_button:
                    pygame.quit()
                    sys.exit()

            # if event.type == pygame.MOUSEBUTTONDOWN: #마우스로 버튼 클릭시 이벤트
            #     if start_button.boundary(pos):
            #         print("clicked the start Button")
            #         screen.fill(black)
            #     if guide_button.boundary(pos):
            #         print("clicked the game guide Button")
            #         screen.fill(black)
            #     if exit_button.boundary(pos):
            #         print("clicked the exit Button")
            #         screen.fill(black)


            if event.type == pygame.MOUSEBUTTONUP: #마우스 버튼을 떼면 생기는 이벤트
                if start_button.isOver(pos):
                    print("start the game")
                    screen.fill(black)
                if guide_button.isOver(pos):
                    print("the game guide")
                    screen.fill(black)
                if exit_button.isOver(pos):
                    print("exit the game")
                    screen.fill(black)
                    pygame.quit()
                    sys.exit()

        #버튼 생성
        

        

if __name__ == '__main__':
    main()
