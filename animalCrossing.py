import pygame as pg
import sys
from os import path
from setting import *
from tilemap import *
from sprites import *
from pygame.locals import QUIT


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Animal Crossing')
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        gameMap_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(gameMap_folder, 'gameMap.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img_scale = pg.transform.scale(self.player_img, (TILESIZE * 2 , TILESIZE * 2))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        # for row, tiles in enumerate(self.map.data): #row == index valud, tiles == string of the characters
        #     for col, tile in enumerate(tiles):
        #         if tile == 'S': # 벽 설정
        #             Wall(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self,col,row) #player위치 설정 가능 #0,0이면 맨 왼쪽 상단에 만들어짐
        self.player = Player(self, 5, 5) #player 위치 임시
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player) #player추적

    def draw_grid(self): #루프를 위해서 두 개 만듬
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE): #높이
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_ing, self.camera.apply_rect(self.map_rect)) #it is not sprite add function o camera class
        # self.draw_grid()
        # self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites: # 모든 sprite 화면에 표시 location 나타냄
            self.screen.blit(sprite.image, self.camera.apply(sprite))#카메라 가져와서 스프라이트에 적용
        pg.display.flip()
        

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

class button(): #버튼 구현 button(image, x축, y축) 
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        
    def draw(self): #draw()
        g.screen.blit(self.image, (self.x,self.y))

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
g = Game()
        #portB =  pygame.Rect(start_icon, WHITE, 66, 92) #곤충 포탈 실험
def start():
    if start_sc == True:
        g.screen.blit(start_bg, (-200,0))
        start_b.draw()
        guide_b.draw()
        exit_b.draw()
        pg.display.update()

def guide():
    if guide_sc == True:
        g.screen.fill(WHITE)
        # screen.blit(start_bg, (-200,0))  #< guide_bg 이미지 구하면 이미지에 맞춰 x축 y축 추가해주기
        exitG_b.draw()
        keepG_b.draw()
        pg.display.update()

def gameMap():
    if gameMap_sc == True: 
        g.new()
        g.run()
        g.show_go_screen()
        pg.display.update()


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

    g.clock.tick()
    global start_sc
    global guide_sc
    global gameMap_sc
    
    while True:

        start()
        guide()
        gameMap()
        # fish()
        # fishG()
        # bugHunt()
        # bugG()
        # store()
        # storeG()
        # home()
        # homeG()

        for event in pg.event.get(): #게임중에 무슨 이벤트인지 for문으로 검사.
            pos = pg.mouse.get_pos()
            
            if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN: #마우스로 버튼 클릭시 이벤트
                if start_b.isOver(pos):
                    start_sc = False
                    gameMap_sc = True

                    g.screen.fill(BLACK)

                elif guide_b.isOver(pos):
                    start_sc = False
                    guide_sc = True
                    g.screen.fill(BLACK)

                elif exit_b.isOver(pos):
                    pg.quit()
                    sys.exit()
        pg.display.flip()

if __name__ == '__main__':
    main()