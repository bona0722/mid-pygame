import pygame

WIDTH  = 1000
HEIGHT = 700
FPS = 60


#define color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#start image
start_bg = pygame.image.load("image/start_background.jpg")
start_icon = pygame.image.load('image/start_icon.png') #start버튼
guide_icon = pygame.image.load('image/guide_icon.png') #guide버튼
exit_icon = pygame.image.load('image/exit_icon.png') #exit버튼

#guide image
# guide_bg = pygame.image.load('image/treebackground.jpg') < guide image 추가하기
keepG_icon = pygame.image.load('image/keepG_icon.png')
exitG_icon = pygame.image.load('image/exitG_icon.png')

#map image
bg = pygame.image.load('image/island.png')
bg_nogo = pygame.image.load('image/island_no-go_area.png')
house = pygame.image.load('image/House.png')
market = pygame.image.load('image/market.png')
fishzone = pygame.image.load('image/fishzone.png')
mos = pygame.image.load('image/mos.png')

#bug image
# background = pygame.image.load(os.path.join(img_folder, "treebackground.jpg")).convert()
# background_img = pygame.transform.scale(background, (WIDTH,HEIGHT))
# background_rect = background_img.get_rect()
# player_img = pygame.image.load(os.path.join(img_folder, "boy.png")).convert()
# bullet_img = pygame.image.load(os.path.join(img_folder, "bomb.png")).convert()
# bug_imgs = []
# bug_list = ['bug_one.png', 'bug_two.png', 'bug_three.png']

#image_scale
img_scale = pygame.transform.scale(bg, (WIDTH, HEIGHT)) #크기변환
img_scale_sea = pygame.transform.scale(bg_nogo, (WIDTH, HEIGHT)) 
img_scale_house = pygame.transform.scale(house, (150, 150))
img_scale_market = pygame.transform.scale(market,(150,150))
img_scale_fishzone = pygame.transform.scale(fishzone,(150,150))
img_scale_mos = pygame.transform.scale(mos,(150,150))

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