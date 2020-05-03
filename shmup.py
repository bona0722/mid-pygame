# Shmup game
import pygame
import random
import os
from setting import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "image")
snd_folder = os.path.join(game_folder, "snd")

WIDTH  = 1000
HEIGHT = 700
FPS = 60

#define color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
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




for img in bug_list :
    bug_imgs.append(pygame.image.load(os.path.join(img_folder, img)).convert())

#모든 게임 사운드
#   

all_sprites = pygame.sprite.Group()
bugs  = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


for i in range(4) :
    b = Bug()
    all_sprites.add(b)
    bugs.add(b)

#점수
score = 0

#Game loop
running = True
while running :
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
        b = Bug()
        all_sprites.add(b)
        bugs.add(b)

    #check to see if a bug hit the player
    hits = pygame.sprite.spritecollide(player, bugs, False, pygame.sprite.collide_circle)
    if hits: #player랑 bug랑 부딪히면 running False로!
        running = False

    #draw / render
    screen.fill(BLACK)
    screen.blit(background_img, background_rect)
    all_sprites.draw(screen) 
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    #after drawing everything flip the display
    pygame.display.flip()

pygame.quit()