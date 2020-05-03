  
import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0 
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
        
    def collide_with_walls(self, dir): #우리가 원할 때만 벽통과
        if dir == 'x':
            hits = pg.sprite.pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits: #무언갈 치면 왼쪽에서 왼쪽 대항 오른쪽에서 오른쪽 대항
                if self.vx > 0: #sprite was moving to the right when it collided woth the wall
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0: #sprite was moving to the right when it collided woth the wall
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits: #무언갈 치면 왼쪽에서 왼쪽 대항 오른쪽에서 오른쪽 대항
                if self.vy > 0: #sprite was moving to the right when it collided woth the wall
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0: #sprite was moving to the right when it collided woth the wall
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt #분수다. 반드시 정수값으로 이동 x losing information됨
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        
        if pg.sprite.spritecollideany(self, self.game.walls):#움직임을 멈춰야함
            self.x -= self.vx * self.game.dt #분수다. 반드시 정수값으로 이동 x losing information됨
            self.y -= self.vy * self.game.dt
            self.rect.topleft = (self.x, self.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE