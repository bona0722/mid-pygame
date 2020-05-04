import pygame as pg
import sys
from tilemap import *
from setting import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        pg.init()
        # self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # pg.display.set_caption('Animal Crossing')
        # self.clock = pg.time.Clock()
        # pg.key.set_repeat(500, 100)
        # self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        self.map = Map(path.join(game_folder, 'map3.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
            
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data): #row == index valud, tiles == string of the characters
            for col, tile in enumerate(tiles):
                if tile == '1': # 벽 설정
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self,col,row)#player위치 설정 가능 #0,0이면 맨 왼쪽 상단에 만들어짐
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
        self.screen.fill(BGCOLOR)
        self.draw_grid()
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