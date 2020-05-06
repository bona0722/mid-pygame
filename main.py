import pygame as pg
import sys
from setting import *
from os import path
from pygame.locals import QUIT
import random
import pytmx
from sprite import *
from tiledmap import *

vec = pg.math.Vector2

score = 0 #곤충잡기 전역변수 돈
hp = 0 #곤충잡기 체력


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Animal Crossing')
        self.clock = pg.time.Clock()
        self.load_data()
        self.load_player_data()

    def draw_text(self, text, font_name, size, color, x, y, align="topleft"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        map_folder = path.join(game_folder, 'maps')
        self.item_images = {}
        self.map = TiledMap(path.join(map_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.raccoon_img = pg.image.load(path.join(img_folder, raccoon_img)).convert_alpha()
        self.raccoon_img = pg.transform.scale(self.raccoon_img, (TILESIZE+32, TILESIZE+32))
        self.tree_img = pg.image.load(path.join(img_folder, tree_img)).convert_alpha()
        self.tree_img = pg.transform.scale(self.tree_img, (TILESIZE+64, TILESIZE+64))
        self.appletree_img = pg.image.load(path.join(img_folder, appletree_img)).convert_alpha()
        self.appletree_img = pg.transform.scale(self.appletree_img, (TILESIZE+64, TILESIZE+64)) 
        self.font_name = pg.font.match_font('arial')

        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
            self.item_images[item] = pg.transform.scale(self.item_images[item], (TILESIZE, TILESIZE))
    
    def load_player_data(self):
            #플레이어 움직임
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'image')
        
        self.playerB_img = pg.image.load(path.join(img_folder, PLAYER_BACK)).convert_alpha()
        self.playerB_img = pg.transform.scale(self.playerB_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerS_img = pg.image.load(path.join(img_folder, PLAYER_STAY)).convert_alpha() # 서 있는 플레이어
        self.playerS_img = pg.transform.scale(self.playerS_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW1_img = pg.image.load(path.join(img_folder, PLAYER_WALK1)).convert_alpha()
        self.playerW1_img = pg.transform.scale(self.playerW1_img, (TILESIZE + 32, TILESIZE+ 32))
        
        self.playerW2_img = pg.image.load(path.join(img_folder, PLAYER_WALK2)).convert_alpha()
        self.playerW2_img = pg.transform.scale(self.playerW2_img, (TILESIZE + 32, TILESIZE+ 32))
        
        self.playerW3_img = pg.image.load(path.join(img_folder, PLAYER_WALK3)).convert_alpha()
        self.playerW3_img = pg.transform.scale(self.playerW3_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW4_img = pg.image.load(path.join(img_folder, PLAYER_WALK4)).convert_alpha()
        self.playerW4_img = pg.transform.scale(self.playerW4_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW5_img = pg.image.load(path.join(img_folder, PLAYER_WALK5)).convert_alpha()
        self.playerW5_img = pg.transform.scale(self.playerW5_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW6_img = pg.image.load(path.join(img_folder, PLAYER_WALK6)).convert_alpha()
        self.playerW6_img = pg.transform.scale(self.playerW6_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW7_img = pg.image.load(path.join(img_folder, PLAYER_WALK7)).convert_alpha()
        self.playerW7_img = pg.transform.scale(self.playerW7_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW8_img = pg.image.load(path.join(img_folder, PLAYER_WALK8)).convert_alpha()
        self.playerW8_img = pg.transform.scale(self.playerW8_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW9_img = pg.image.load(path.join(img_folder, PLAYER_WALK9)).convert_alpha()
        self.playerW9_img = pg.transform.scale(self.playerW9_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerW10_img = pg.image.load(path.join(img_folder, PLAYER_WALK10)).convert_alpha()
        self.playerW10_img = pg.transform.scale(self.playerW10_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerBcatch1_img = pg.image.load(path.join(img_folder, PLAYER_BACK_CATCH1)).convert_alpha()
        self.playerBcatch1_img = pg.transform.scale(self.playerBcatch1_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerBcatch2_img = pg.image.load(path.join(img_folder, PLAYER_BACK_CATCH2)).convert_alpha()
        self.playerBcatch2_img = pg.transform.scale(self.playerBcatch2_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerBcatch3_img = pg.image.load(path.join(img_folder, PLAYER_BACK_CATCH3)).convert_alpha()
        self.playerBcatch3_img = pg.transform.scale(self.playerBcatch3_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerside1catch1_img = pg.image.load(path.join(img_folder, PLAYER_SIDE1_CATCH1)).convert_alpha()
        self.playerside1catch1_img = pg.transform.scale(self.playerside1catch1_img, (TILESIZE + 32, TILESIZE+ 32))
         
        self.playerside1catch2_img = pg.image.load(path.join(img_folder, PLAYER_SIDE1_CATCH2)).convert_alpha()
        self.playerside1catch2_img = pg.transform.scale(self.playerside1catch2_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerside1catch3_img = pg.image.load(path.join(img_folder, PLAYER_SIDE1_CATCH3)).convert_alpha()
        self.playerside1catch3_img = pg.transform.scale(self.playerside1catch3_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerside2catch1_img = pg.image.load(path.join(img_folder, PLAYER_SIDE2_CATCH1)).convert_alpha()
        self.playerside2catch1_img = pg.transform.scale(self.playerside2catch1_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerside2catch2_img = pg.image.load(path.join(img_folder, PLAYER_SIDE2_CATCH2)).convert_alpha()
        self.playerside2catch2_img = pg.transform.scale(self.playerside2catch2_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerside2catch3_img = pg.image.load(path.join(img_folder, PLAYER_SIDE2_CATCH3)).convert_alpha()
        self.playerside2catch3_img = pg.transform.scale(self.playerside2catch3_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerstaycatch1_img = pg.image.load(path.join(img_folder, PLAYER_STAY_CATCH1)).convert_alpha()
        self.playerstaycatch1_img = pg.transform.scale(self.playerstaycatch1_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerstaycatch2_img = pg.image.load(path.join(img_folder, PLAYER_STAY_CATCH2)).convert_alpha()
        self.playerstaycatch2_img = pg.transform.scale(self.playerstaycatch2_img, (TILESIZE + 32, TILESIZE+ 32))

        self.playerstaycatch3_img = pg.image.load(path.join(img_folder, PLAYER_STAY_CATCH3)).convert_alpha()
        self.playerstaycatch3_img = pg.transform.scale(self.playerstaycatch3_img, (TILESIZE + 32, TILESIZE+ 32))


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.raccoon_dog = pg.sprite.Group()
        self.trees = pg.sprite.Group()
        self.appletrees = pg.sprite.Group()
        self.items = pg.sprite.Group()
        for tile_object in self.map.tmxdata.objects: #모든 오브젝트 정의
            #속성은 dictionary
            obj_center = vec(tile_object.x + tile_object.width /2
                             ,tile_object.y+ tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player_1(self, tile_object.x, tile_object.y)
            # if tile_object.name == 'raccoon_dog' :
            #     Raccoon(self, tile_object.x, tile_object.y)
            #     Obstacle(self, tile_object.x, tile_object.y, 
            #         5, 5)
            if tile_object.name == 'trees' :
                Tree(self, tile_object.x, tile_object.y)
                Obstacle(self, tile_object.x, tile_object.y, 
                    0, 0)
            if tile_object.name == 'appletrees' :
                Appletree(self, tile_object.x, tile_object.y)
                Obstacle(self, tile_object.x, tile_object.y, 
                        0,0)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, 
                        tile_object.width, tile_object.height)
            if tile_object.name in ['apple','bug1', 'bug2', 'bug3', 'raccoon_dog']:
                Item(self, obj_center, tile_object.name)
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
        global score
        ending_b = button(ending, 0, 0)
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player) #player추적
        hits = pg.sprite.pygame.sprite.spritecollide(self.player, self.items, False)
        keys = pg.key.get_pressed()
        for hit in hits:
            if hit.type == 'apple':
                hit.kill()
                score += APPLE_AMOUNT
                
            if hit.type == 'bug1' and keys[pg.K_SPACE]:
                hit.kill()
                score += BUG1_AMOUNT
            if hit.type == 'bug2' and keys[pg.K_SPACE]:
                hit.kill()
                score += BUG2_AMOUNT
            if hit.type == 'bug3' and keys[pg.K_SPACE]:
                hit.kill()
                score += BUG3_AMOUNT
            if hit.type == 'raccoon_dog' and keys[pg.K_SPACE]:
                if score >= 1390: 
                    break
                elif score > 1000:
                    break
                else: 
                    break


    def draw(self):
        global money_b
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites: # 모든 sprite 화면에 표시 location 나타냄
            self.screen.blit(sprite.image, self.camera.apply(sprite))#카메라 가져와서 스프라이트에 적용
            money_b.draw()
            self.draw_text('Bell: {}'.format(score), self.font_name, 27, BLACK, 70, 70)

        pg.display.flip()
        

    def events(self):
        global start_sc
        # catch all events here
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

class Item(pg.sprite.Sprite):
    def __init__(self, game, pos, type):
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type] #어떤 유형의 이미지든 일치.
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.center = pos #위치선정

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
exitG_b = button(exitG_icon, 900, 50)
keepG_b = button(keepG_icon, 900, 200)
backG_b = button(backG_icon, 900, 350)
#벨추가
money_b = button(money_icon, 40,20)

#초기화 pygame and create window
pg.init()
pg.mixer.init() #소리에 필수
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My game")
clock = pg.time.Clock()



def start():
    if start_sc == True:
        pg.mixer.Sound.play(intro_bgm)
        g.screen.blit(start_bg, (0,0))
        start_b.draw()
        guide_b.draw()
        exit_b.draw()
        pg.display.update()
    else : 
        pg.mixer.Sound.stop(intro_bgm)
gC = 0 #guide 스크린 전환 카운트
def guide():
    global gC
    global guide_sc
    if guide_sc == True:
        pg.mixer.Sound.play(nbt)

        if gC == 0:
            g.screen.blit(guide_1,(0, 0))
            exitG_b.draw()
            keepG_b.draw()
        if gC == 1:
            g.screen.blit(guide_2,(0, 0))
            backG_b.draw()
            exitG_b.draw()
            keepG_b.draw()
        if gC == 2:
            g.screen.blit(guide_3,(0, 0))
            backG_b.draw()
            exitG_b.draw() 
    else : 
        pg.mixer.Sound.stop(nbt)          
       

def gameMap():
    global gameMap_sc
    if gameMap_sc == True: 
        pg.mixer.Sound.play(main_bgm)
        g.new()
        g.run()
        pg.display.update()
    else : 
        pg.mixer.Sound.stop(main_bgm)
g = Game()

g.clock.tick()

# score = 100
while True:
    
    start()
    guide()
    gameMap()


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

            if keepG_b.isOver(pos):
                gC+=1
            if backG_b.isOver(pos):
                gC-=1
            if exitG_b.isOver(pos):
                guide_sc = False
                start_sc = True
                g.screen.fill(BLACK)
            
            pg.display.update()
        
            
    pg.display.flip()

