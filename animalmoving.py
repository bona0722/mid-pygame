#useless program
# import sys
# import pygame
# from pygame.locals import QUIT



# pygame.init() #초기화를 해줘야함
# width, height = 1000,700
# pygame.display.set_caption("animal game") #게임 제목을 써줌. 화면이 꺼지기 전까지 제목이 계속 유지되므로 전역변수로 설정하기
# screen = pygame.display.set_mode((width, height)) #x축,y축 생성
#  # 화면을 초기화하거나 화면에 데이터 추가하는 변수

# bg = pygame.image.load('image/island.png')
# house = pygame.image.load('image/House.png')
# market = pygame.image.load('image/market.png')
# fishzone = pygame.image.load('image/fishzone.png')
# mos = pygame.image.load('image/mos.png')
# img_scale = pygame.transform.scale(bg, (width, height)) #크기변환
# img_scale_house = pygame.transform.scale(house, (150, 150))
# img_scale_market = pygame.transform.scale(market,(150,150))
# img_scale_fishzone = pygame.transform.scale(fishzone,(150,150))
# img_scale_mos = pygame.transform.scale(mos,(150,150))
# clock = pygame.time.Clock() #< #화면을 초 당 몇 번 출력하는지. 게임의 fps설정 가능

# def main(): #게임을 실행할 때 게임에서 발생한 event에 대한 설정이나 사용자의 게임 알고리즘이 여기서 작성돼야함
# #clock.tick() #fps를 10으로 설정. 초 당 화면 10번 출력. 값이 높을수록 CPU 많이 씀.10 30 60으로 설정함
#     white = (255, 255, 255)
#     black = (0, 0, 0)
#     pos_x= 200
#     pos_y = 200

#     while True: #while로 구현
#         clock.tick(100)
#         for event in pygame.event.get(): 
#             #게임중에 마우스 클릭 등 이벤트 발생하면 인지하고 무슨 이벤트인지 for문으로 검사.
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()

#         key_event = pygame.key.get_pressed()

#         if key_event[pygame.K_LEFT]:
#             pos_x -= 1
#         if key_event[pygame.K_LCTRL] and key_event[pygame.K_LEFT]:
#             pos_x -= 2

#         if key_event[pygame.K_RIGHT]:
#             pos_x += 1
#         if key_event[pygame.K_LCTRL] and key_event[pygame.K_RIGHT]:
#             pos_x += 2

#         if key_event[pygame.K_UP]:
#             pos_y -= 1
#         if key_event[pygame.K_LCTRL] and key_event[pygame.K_UP]:
#             pos_y -= 2

#         if key_event[pygame.K_DOWN]:
#             pos_y += 1
#         if key_event[pygame.K_LCTRL] and key_event[pygame.K_DOWN]:
#             pos_y += 2

#         screen.fill(black)
#         screen.blit(img_scale, (0,0))
#         screen.blit(img_scale_house, (500,250))
#         screen.blit(img_scale_market, (150,200))
#         screen.blit(img_scale_fishzone, (700,130))
#         screen.blit(img_scale_mos,(680,400))
#         pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
#         pygame.display.update()

# if __name__ == '__main__':
#     main()