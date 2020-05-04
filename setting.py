import pygame as pg
import os


#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
BGCOLOR = DARKGREY


TILESIZE = 64 #숫자가 크면 탐험 느낌이 더 날 것이다.
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#player setting
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'pstay.png'

#tile image
SEA_IMG ='sea.png'

#start image
start_bg = pg.image.load("image/start_background.jpg")
start_icon = pg.image.load('image/start_icon.png') #start버튼
guide_icon = pg.image.load('image/guide_icon.png') #guide버튼
exit_icon = pg.image.load('image/exit_icon.png') #exit버튼


#guide image
# guide_bg = pg.image.load('image/treebackground.jpg') < guide image 추가하기
keepG_icon = pg.image.load('image/keepG_icon.png')
exitG_icon = pg.image.load('image/exitG_icon.png')


#map image
bg = pg.image.load('image/island.png')
bg_nogo = pg.image.load('image/island_no-go_area.png')
house = pg.image.load('image/House.png')
market = pg.image.load('image/market.png')
fishzone = pg.image.load('image/fishzone.png')
mos = pg.image.load('image/mos.png')


#bug image
background = pg.image.load("image/treebackground.jpg")
background_img = pg.transform.scale(background, (WIDTH,HEIGHT))
background_rect = background_img.get_rect()
player_img = pg.image.load("image/boy.png")
bullet_img = pg.image.load( "image/bomb.png")
bug_imgs = []
bug_list = ['bug_one.png', 'bug_two.png', 'bug_three.png']


#image_scale
img_scale = pg.transform.scale(bg, (WIDTH, HEIGHT)) #크기변환
img_scale_sea = pg.transform.scale(bg_nogo, (WIDTH, HEIGHT)) 
img_scale_house = pg.transform.scale(house, (150, 150))
img_scale_market = pg.transform.scale(market,(150,150))
img_scale_fishzone = pg.transform.scale(fishzone,(150,150))
img_scale_mos = pg.transform.scale(mos,(150,150))

#screen
start_sc = True #첫화면
guide_sc = False #설명서
gameMap_sc = False #게임 전체 맵
fish_sc = False #낚시맵 fishing
fishG_sc = False #낚시 설명 fishing Guide
bugHunt_sc = False #곤충맵 bug hunting
bugG_sc = False #곤충잡기 설명 bug hunting Guide
store_sc = False #상점맵
storeG_sc = False #물건 구입 설명
home_sc = False #집맵
homeG_sc = False #집꾸미기 설명 home Interior Guide
