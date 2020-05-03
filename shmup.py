# Shmup game
import pygame
import random
import sys
import os
from setting_ho import *
from pygame.locals import QUIT

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "image")
snd_folder = os.path.join(game_folder, "snd")


#text가 필요할 떄마다 쓸 수 있음!
#일반 글꼴 사용
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y) :
    font = pygame.font.Font(font_name, size)
    #true와 false는 텍스트를 원하는지 여부를 알리는 것 false는 픽셀 뚜렸 True는 흐릿
    #anti-aliased 처리된 텍스트
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def newbug():
    b = Bug()
    all_sprites.add(b)
    bugs.add(b)

def draw_shield_bar(surf, x, y, pct) :
    if pct < 0 :
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT =10
    fill = (pct/100)*BAR_LENGTH
    #채워질 사각형
    outline_rect = pygame.Rect(x,y,BAR_LENGTH, BAR_HEIGHT)
    #채워진 사각형
    fill_rect = pygame.Rect(x,y,fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class button(): #버튼 구현 button(image, x축, y축) 
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image
        
    def draw(self): #draw()
        screen.blit(self.image, (self.x,self.y))

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

#portB =  pygame.Rect(start_icon, white, 66, 92) #곤충 포탈 실험
def start():
    if start_sc == True:
        screen.blit(start_bg, (-200,0))
        start_b.draw()
        guide_b.draw()
        exit_b.draw()
        pygame.display.update()

def guide():
    if guide_sc == True:
        screen.fill(WHITE)
        # screen.blit(start_bg, (-200,0))  #< guide_bg 이미지 구하면 이미지에 맞춰 x축 y축 추가해주기
        exitG_b.draw()
        keepG_b.draw()
        pygame.display.update()

class Player(pygame.sprite.Sprite) : #player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (100,100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #원형스타일로 해서 충돌 때 정확하게하려고 설정
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 100
        self.speedx = 0
        self.shield = 100
        
    
    def update(self) :
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] :
            self.speedx = -5
        if keystate[pygame.K_RIGHT] :
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH :
            self.rect.right = WIDTH
        if self.rect.left < 0 :
            self.rect.left = 0

    def shoot(self) :
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_snd.play()

class Bug(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(bug_imgs)
        self.image_orig.set_colorkey(WHITE)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3,3)
        self.rot = 0 #회전변수
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()
        #시계가 시작된 이후에 게임시작되었고 이미지가 변할 떄마다 업데이트
    
    def rotate(self) :
        now = pygame.time.get_ticks()
        if now - self.last_update > 50 :
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pygame.transform.rotate(self.image_orig, self.rot)
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def update(self) :
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite) : #총알
    def __init__(self,x,y) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (30,30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 #화면에서 올라가는 거는 음수로 표현

    def update(self) :
        self.rect.y += self.speedy
        #kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill() #sprite를 가져와서 그룹에서 제거하는 명령
         

    

#초기화 pygame and create window
pygame.init()
pygame.mixer.init() #소리에 필수
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

#gameover screen
def show_go_screen():
    screen.blit(background_img, background_rect)
    draw_text(screen, "CATCH BUGS", 64,WIDTH/2, HEIGHT/4)
    draw_text(screen, "Arrow keys move, Space to fire", 22,WIDTH/2, HEIGHT/2)
    draw_text(screen, "Press a key to begin", 18, WIDTH/2, HEIGHT*3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# 게임 그래픽 로드
background = pygame.image.load(os.path.join(img_folder, "treebackground.jpg")).convert()
background_img = pygame.transform.scale(background, (WIDTH,HEIGHT))
background_rect = background_img.get_rect()
player_img = pygame.image.load(os.path.join(img_folder, "boy.png")).convert()
bullet_img = pygame.image.load(os.path.join(img_folder, "bomb.png")).convert()
bug_imgs = []
bug_list = ['bug_one.png', 'bug_two.png', 'bug_three.png']


for img in bug_list :
    bug_imgs.append(pygame.image.load(os.path.join(img_folder, img)).convert())

#모든 게임 사운드
shoot_snd = pygame.mixer.Sound(os.path.join(snd_folder,'hit.wav'))

all_sprites = pygame.sprite.Group()
bugs  = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


for i in range(6) :
    newbug()

#점수
score = 0

#Game loop

#게임이 시작할지 말지 , 끝났을 때 어떻게 해야하는지 말해줌
game_over = True
running = True
start_sc = True
guide_sc = True
st = True
while st :
    start()
    for event in pygame.event.get(): #게임중에 무슨 이벤트인지 for문으로 검사.
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #마우스로 버튼 클릭시 이벤트
                if start_b.isOver(pos):
                    start_sc = False
                    gameMap_sc = True
                    st = False

                elif guide_b.isOver(pos):
                    start_sc = False
                    guide_sc = True
                    guide()

                elif exit_b.isOver(pos):
                    pygame.quit()
                    sys.exit()


while running :

    if game_over :
        show_go_screen()#game over screen
        game_over = False
        all_sprites = pygame.sprite.Group()
        bugs  = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)


        for i in range(6) :
            newbug()

        #점수
        score = 0

    #keep loop running at the right speed
    clock.tick(FPS)
    #process input(events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE :
                player.shoot()
        
    #update
    all_sprites.update()

    #check to see if a bullet hit a bug
    hits = pygame.sprite.groupcollide(bugs, bullets, True, True)
    
    for hit in hits :
        score += hit.radius
        newbug()

    #check to see if a bug hit the player
    hits = pygame.sprite.spritecollide(player, bugs, True, pygame.sprite.collide_circle)
    for hit in hits: #player랑 bug랑 부딪히면 running False로!
        player.shield -= 30
        if player.shield <= 0 :
            game_over = True
            # running = False

    #draw / render
    screen.fill(BLACK)
    screen.blit(background_img, background_rect)
    all_sprites.draw(screen) 
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    draw_shield_bar(screen, 5,5, player.shield)
    #after drawing everything flip the display
    pygame.display.flip()

pygame.quit()