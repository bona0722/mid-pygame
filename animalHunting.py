import sys, pygame

pygame.init() #초기화를 해줘야함.

pygame.display.set_caption("Window size 400") #게임 제목을 써줌. 화면이 꺼지기 전까지 제목이 계속 유지되므로 전역변수로 설정하기
screen = pygame.display.set_mode((1000,700)) #x축,y축 생성
 # 화면을 초기화하거나 화면에 데이터 추가하는 변수
start_backg = pygame.image.load(os.path.join("image", "Hunting_background.jpg")).convert()

for event in 