
def start(): #start맵에서 나와야하는 화면
    start_b = button(start_icon, 500, 550)
    guide_b = button(guide_icon, 650, 550)
    exit_b = button(exit_icon, 800, 550)

    if start_sc == True:
        screen.blit(start_bg, (-200,0))
        start_b.draw()
        guide_b.draw()
        exit_b.draw()
        pygame.display.update()

    def guide(): #첫화면에 있는 설명
        exitG_b = button(exitG_icon, x,y) < 설명 종료 버튼 이미지 구하고 이미지에 맞춰 x축 y축 추가해주기
        keepG_b = button(keepG_icon, x, y) < 설명 계속 버튼 (즉 설명 중 다음 스크립트로 넘어가는 버튼) 정하고 이미지에 맞춰 x축 y축 추가해주기
        if guide_sc == True:
            screen.blit(guide_bg, ())  < guide_bg 이미지 구하면 이미지에 맞춰 x축 y축 추가해주기
            exitG_b.draw()
            keepG_b.draw()
            pygame.display.update()


            
    # def gameMap(self):
    #     if gameMap_sc == True: 

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