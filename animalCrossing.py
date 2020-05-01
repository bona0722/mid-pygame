import pygame, sys, os
from pygame.locals import QUIT

pygame.init() #초기화를 해줘야함.
pygame.display.set_caption("Window size 400") #게임 제목을 써줌. 화면이 꺼지기 전까지 제목이 계속 유지되므로 전역변수로 설정하기
screen = pygame.display.set_mode((1000,700)) #x축,y축 생성
 # 화면을 초기화하거나 화면에 데이터 추가하는 변수
start_backg = pygame.image.load(os.path.join("image", "start_background.jpg")).convert()
saddleBrown = (139, 69, 19) #start button color
gray = (128,128,128)


class button(): #버튼 구현 button
    def __init__(self, win, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.win = win
        
    def draw(self): #버튼을 그려줌
        pygame.draw.rect(self.win , self.color, (self.x, self.y, self.width, self.height))

    # def text(self, text): #버튼에 폰트를 적어줌


    def boundary(self): #mouse가 버튼 내 좌표에 있으면 True반환
        print(self.x, self.y , self.width, self.height)
        if :
            return True
def moving(): #걷는 함수, 방향키 > 걷는다. ctrl + 방향키를 누르면 뛸 수 있다.
        white = (255, 255, 255)
        black = (0, 0, 0)
        pos_x= 200
        pos_y = 200
            if key_event[pygame.K_LEFT]: 
                pos_x -= 1
            if key_event[pygame.K_LCTRL] and key_event[pygame.K_LEFT]:
                pos_x -= 2

            if key_event[pygame.K_RIGHT]:
                pos_x += 1
            if key_event[pygame.K_LCTRL] and key_event[pygame.K_RIGHT]:
                pos_x += 2

            if key_event[pygame.K_UP]:
                pos_y -= 1
            if key_event[pygame.K_LCTRL] and key_event[pygame.K_UP]:
                pos_y -= 2

            if key_event[pygame.K_DOWN]:
                pos_y += 1
            if key_event[pygame.K_LCTRL] and key_event[pygame.K_DOWN]:
                pos_y += 2

def main(): #게임을 실행할 때 게임에서 발생한 event에 대한 설정이나 사용자의 게임 알고리즘이 여기서 작성돼야함

        start_button = button(screen, saddleBrown, 80, 50, 250, 80, '게임시작')
        guide_button = button(screen, saddleBrown, 80, 150, 250, 80, '설명')
        exit_button = button(screen, saddleBrown, 80, 250, 250, 80, '종료')

        while True: #while로 구현
            for event in pygame.event.get(): 
                #게임중에 마우스 클릭 등 이벤트 발생하면 인지하고 무슨 이벤트인지 for문으로 검사.
                if event.type == QUIT:
                    if exit_button:
                        pygame.quit()
                        sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.boundary() or guide_button.boundary() or exit_button.boundary(): 
                    print("clicked the Button")
            if event.type == pygame.MOUSEBUTTONUP:
                if start_button.boundary():
                    print("start the game")
                elif guide_button.boundary():
                    print("the game guide")
                elif exit_button.boundary():
                    print("exit the game")
            
            screen.blit(start_backg, (-200,0))
            
            #버튼 생성
            start_button.draw()
            guide_button.draw()
            exit_button.draw()
            #pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
            pygame.display.flip()
            

if __name__ == '__main__':
    main()