import pygame as pg
# import os

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
FPS = 100
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
GROUND_IMG = 'ground.png'


PLAYER_STAY= 'pstay.png' #플레이어 서있는 모습
PLAYER_BACK = 'pback.png' #플레이어 뒷모습
PLAYER_WALK1 = 'pwalk1.png' #플레이어 오른쪽 옆으로 걷는 모습 왼발이 앞
PLAYER_WALK2 = 'pwalk2.png' #플레이어 오른쪽 옆으로 걷는 모습 오른발 접음
PLAYER_WALK3 = 'pwalk3.png' #플레이어 오른쪽 옆으로 걷는 모습 오른발 앞
PLAYER_WALK4 = 'pwalk4.png' #플레이어 뒤로 뛰는 모습 왼발이 앞
PLAYER_WALK5 = 'pwalk5.png' #플레이어 뒤로 뛰는 모습 오른발이 앞
PLAYER_WALK6 = 'pwalk6.png' #플레이어 앞으로 뛰는 모습 왼발이 앞
PLAYER_WALK7 = 'pwalk7.png' #플레이어 앞으로 뛰는 모습 왼발이 앞
PLAYER_WALK8 = 'pwalk8.png' #플레이어 왼쪽 옆으로 걷는 모습 왼발 앞
PLAYER_WALK9 = 'pwalk9.png' #플레이어 왼쪽 옆으로 걷는 모습 왼발 접음
PLAYER_WALK10 = 'pwalk10.png' #플레이어 왼쪽 옆으로 걷는 모습 오른발 앞

PLAYER_BACK_CATCH1 ='backcatch1.png'
PLAYER_BACK_CATCH2 ='backcatch2.png'
PLAYER_BACK_CATCH3 ='backcatch3.png'
PLAYER_STAY_CATCH1 ='net4.png'
PLAYER_STAY_CATCH2 ='Net5.png'
PLAYER_STAY_CATCH3 ='Net6.png'
PLAYER_SIDE1_CATCH1 ='Net7.png'
PLAYER_SIDE1_CATCH2 ='Net8.png'
PLAYER_SIDE1_CATCH3 ='Net9.png'
PLAYER_SIDE2_CATCH1 ='Net12.png'
PLAYER_SIDE2_CATCH2 ='Net11.png'
PLAYER_SIDE2_CATCH3 ='Net10.png'

#start image
start_bg = pg.image.load("image/start_background.jpg")
start_bg = pg.transform.scale(start_bg, (WIDTH,HEIGHT))
start_icon = pg.image.load('image/start_icon.png') #start버튼
guide_icon = pg.image.load('image/guide_icon.png') #guide버튼
exit_icon = pg.image.load('image/exit_icon.png') #exit버튼

#sound

#gamemap image
money_icon = pg.image.load("image/money_icon.png")
money_icon = pg.transform.scale(money_icon, (150, 100))

#guide image
keepG_icon = pg.image.load('image/keepG_icon.png')
keepG_icon = pg.transform.scale(keepG_icon, (TILESIZE*2, TILESIZE *2)) 

exitG_icon = pg.image.load('image/exitG_icon.png')
exitG_icon = pg.transform.scale(exitG_icon, (TILESIZE*2, TILESIZE *2))

backG_icon = pg.image.load('image/backG_icon.png')
backG_icon = pg.transform.scale(backG_icon, (TILESIZE*2, TILESIZE *2)) 

guide_1 = pg.image.load('image/guide_1.png')
guide_1 = pg.transform.scale(guide_1, (WIDTH, HEIGHT))
guide_2 = pg.image.load('image/guide_2.png')
guide_2 = pg.transform.scale(guide_2, (WIDTH, HEIGHT))
guide_3 = pg.image.load('image/guide_3.png')
guide_3 = pg.transform.scale(guide_3, (WIDTH, HEIGHT))


#map image
bg = pg.image.load('image/island.png')
bg_nogo = pg.image.load('image/island_no-go_area.png')
house = pg.image.load('image/House.png')
market = pg.image.load('image/market.png')
fishzone = pg.image.load('image/fishzone.png')
mos = pg.image.load('image/mos.png')
img_scale_mos = pg.transform.scale(mos,(150,150))


#bug image
background = pg.image.load("image/treebackground.jpg")
background_img = pg.transform.scale(background, (WIDTH,HEIGHT))
background_rect = background_img.get_rect()
player_img = pg.image.load("image/pstay.png")
bullet_img = pg.image.load( "image/bomb.png")
bug_imgs = []
bug_list = ['bug_one.png', 'bug_two.png', 'bug_three.png']

#finish
ending = pg.image.load("image/ending.png")
ending = pg.transform.scale(ending, (WIDTH, HEIGHT))
#나무 이미지
appletree_img = 'AppleTree.png'
tree_img = 'Tree.png'
#너굴 이미지
raccoon_img = 'raccoon.png'

#image_scale
img_scale = pg.transform.scale(bg, (WIDTH, HEIGHT)) #크기변환


#screen
start_sc = True #첫화면
guide_sc = False #설명서
gameMap_sc = False #게임 전체 맵


#sound
pg.mixer.init()
main_bgm = pg.mixer.Sound('snd/animalcrossing_bgm.wav')
intro_bgm = pg.mixer.Sound('snd/animalcrossing_intro.wav')
hit = pg.mixer.Sound('snd/hit.wav')
nbt = pg.mixer.Sound('snd/nabi_bobet_tau.wav')
runing = pg.mixer.Sound('snd/Run.wav')

#layer
ITEMS_LAYER = 1

#items
ITEM_IMAGES = {'apple': 'apple.png', 'bug1' : 'bug_one.png', 'bug2' : 'bug_two.png','bug3' : 'bug_three.png', 'raccoon_dog' : 'raccoon.png'}
APPLE_AMOUNT = 50
BUG1_AMOUNT = 20
BUG2_AMOUNT = 60
BUG3_AMOUNT = 100