import pygame, sys, os
from pygame.locals import QUIT

pygame.init() #초기화를 해줘야함.
pygame.display.set_caption("Animal Crossing") #게임 제목을 써줌. 화면이 꺼지기 전까지 제목이 계속 유지되므로 전역변수로 설정하기
width, height = 1000, 700
screen = pygame.display.set_mode((width, height)) #x축,y축 생성
 # 화면을 초기화하거나 화면에 데이터 추가하는 변수
clock = pygame.time.Clock() #< #화면을 초 당 몇 번 출력하는지. 게임의 fps설정 가능

saddleBrown = (139, 69, 19) #button color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

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


class Entity(pygame.sprite.Sprite) : #sprite init
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)

class Player(Entity) : #player 관련 함수 및 player 기본설정
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

class button(): #버튼 구현 button(screen, color, x축, y축, 가로, 세로) 
    def __init__(self, win, bColor, x, y, width, height):
        self.win = win
        self.bColor = bColor

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        # self.click = pygame.mouse.get_pressed()
        
    def draw(self, text = '', tColor = 0): #draw(텍스트, 텍스트 컬러)
        #make a rectangle button
        pygame.draw.rect(self.win , self.bColor, (self.x, self.y, self.width+4, self.height+2))

        #font
        font = pygame.font.SysFont('굴림', self.height)
        text = font.render(text, True, tColor)
        self.win.blit(text, (self.x  + 1, self.y + 2))

    def boundary(self, pos): #mouse가 버튼 내 좌표에 있으면 True반환. boundary(pygame.mouse.get_pos()
        if pos[0] < self.x + self.width and pos[0] > self.x:
            if pos[1] < self.y + self.height and pos[1] > self.y:
                return True
        return False


def main(): #게임을 실행할 때 게임에서 발생한 event에 대한 설정이나 사용자의 게임 알고리즘이 여기서 작성돼야함
    
    start_button = button(screen, saddleBrown, 80, 50, 250, 80)
    guide_button = button(screen, saddleBrown, 80, 150, 250, 80)
    exit_button = button(screen, saddleBrown, 80, 250, 250, 80)
    clock.tick(100)

    while True: #while로 구현
        
        for event in pygame.event.get(): #게임중에 무슨 이벤트인지 for문으로 검사.
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                if exit_button:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: #마우스로 버튼 클릭시 이벤트
                if start_button.boundary(pos):
                    print("clicked the start Button")
                    screen.fill(black)
                if guide_button.boundary(pos):
                    print("clicked the game guide Button")
                    screen.fill(black)
                if exit_button.boundary(pos):
                    print("clicked the exit Button")
                    screen.fill(black)


            if event.type == pygame.MOUSEBUTTONUP: #마우스 버튼을 떼면 생기는 이벤트
                if start_button.boundary(pos):
                    print("start the game")
                    screen.fill(black)
                if guide_button.boundary(pos):
                    print("the game guide")
                    screen.fill(black)
                if exit_button.boundary(pos):
                    print("exit the game")
                    screen.fill(black)
                    pygame.quit()
                    sys.exit()
        

        screen.blit(start_bg, (-200,0))
            
        start_button.draw('START', black)
        guide_button.draw('GUIDE', black)
        exit_button.draw('EXIT', black)
        pygame.display.update()

        # screen.blit(img_scale_house, (500,250))
        # screen.blit(img_scale_market, (150,200))
        # screen.blit(img_scale_fishzone, (700,130))
        # screen.blit(img_scale_mos,(680,400))
        # pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
        
if __name__ == '__main__':
    main()