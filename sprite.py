import pygame as pg
from random import uniform, choice, randint
from setting import *
vec = pg.math.Vector2



c = 0
a = 0
b = 0
class Player_1(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.playerS_img #플레이어 이미지 설정
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def get_keys(self):
        global a, b, c
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            a = 1
            self.vel.x = -PLAYER_SPEED
            if c == 0 :
                self.image = self.game.playerW8_img
            elif c == 1 :
                self.image = self.game.playerW9_img
            elif c == 2 :
                self.image = self.game.playerW10_img
                c = -1
            c+=0.25
        if keys[pg.K_RIGHT]:
            a = 2
            self.vel.x = PLAYER_SPEED
            if c == 0 :
                self.image = self.game.playerW1_img
            elif c == 1 :
                self.image = self.game.playerW2_img
            elif c == 2 :
                self.image = self.game.playerW3_img
                c = -1
            c+=0.25            
        if keys[pg.K_UP]:
            a=3
            self.vel.y = -PLAYER_SPEED
            if c == 0 :
                self.image = self.game.playerB_img
            elif c == 1 :
                self.image = self.game.playerW4_img
            elif c == 2 :
                self.image = self.game.playerW5_img
                c = -1
            c+=0.25
        if keys[pg.K_DOWN]:
            a=4
            self.vel.y = PLAYER_SPEED
            if c == 0 :
                self.image = self.game.playerS_img
            elif c == 1 :
                self.image = self.game.playerW6_img
            elif c == 2 :
                self.image = self.game.playerW7_img
                c = -1
            c+=0.25


        if keys[pg.K_SPACE] :
            if a == 1 : #왼
                self.vel.x = 0
                if b == 0:
                    self.image = self.game.playerside1catch1_img 
                elif b == 1 :
                    self.image = self.game.playerside1catch2_img
                elif b == 2 :
                    self.image = self.game.playerside1catch3_img
                    b = -1
                b += 1
            if a == 2 : #오
                self.vel.x = 0
                if b == 0 :
                    self.image = self.game.playerside2catch1_img
                elif b == 1 :
                    self.image = self.game.playerside2catch2_img
                elif b == 2 :
                    self.image = self.game.playerside2catch3_img
                    b = -1
                b += 1
            if a == 3 :
                self.vel.y = 0
                if b == 0 :
                    self.image = self.game.playerBcatch1_img
                elif b == 1 :
                    self.image = self.game.playerBcatch2_img
                elif b == 2 :
                    self.image = self.game.playerBcatch3_img
                    b = -1
                b += 1
            if a == 4 : #밑
                self.vel.y = 0
                if b == 0 :
                    self.image = self.game.playerstaycatch1_img
                elif b == 1 :
                    self.image = self.game.playerstaycatch2_img
                elif b == 2 :
                    self.image = self.game.playerstaycatch3_img
                    b = -1
                b += 1
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
    def collide_with_walls(self, dir): #우리가 원할 때만 벽통과
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
            

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.sea_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Raccoon(pg.sprite.Sprite):
    def __init__(self, game, x, y) :
        self.groups = game.all_sprites, game.raccoon_dog
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.raccoon_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
    def update(self) :
        # self.image = pg.transform.scale(self.game.raccoon_img, )
        self.rect.center = self.pos

class Tree(pg.sprite.Sprite) :
    def __init__(self, game, x, y) :
        self.groups = game.all_sprites, game.trees
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.tree_img
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.rect.center = self.pos

    def update(self) :
        self.rect.center = self.pos

class Appletree(pg.sprite.Sprite) :
    def __init__(self, game, x, y) :
        self.groups = game.all_sprites, game.appletrees
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.appletree_img
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.rect.center = self.pos

    def update(self) :
        self.rect.center = self.pos

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups =  game.walls#, game.raccoon_dog, game.appletrees, game.trees
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y