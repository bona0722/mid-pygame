import pygame as pg
import pytmx
from setting import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip()) #텍스트 파일에 자동적으로 \n있는 거 삭제

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        
class Camera:
    def __init__(self, width,height):
        self.camera = pg.Rect(0,0,width,height) #offset 추적
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft) #rect움직임

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self,target): #sprite 따라감 s,y위치조정
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        #rimit scaralling to map size
        x = min(0, x)# offset이 0보다 안 큼 양수가 안 됨. 0을 안 떠남. 카메라가 빈 공간을 비추지 않는다.
        y = min(0, y)
        #오른쪽과 왼쪽은 약간의 사이즈 차이가 있음 여분이 남는다.
        ##텍스트 파일에 자동적으로 \n있는 거 삭제 9번째 줄에서 line을 추가할 때 strip()해준다.
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y) #높이에서 화면 높이만큼 빼기
        self.camera = pg.Rect(x, y, self.width,self.height)


class TiledMap:
    def __init__(self, filename): #지도 load
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth #tile의 width
        self.height = tm.height * tm.tileheight #tile의 height
        self.tmxdata = tm

    def render(self, surface): #모든 타일을 보고 타일을 그림
        ti = self.tmxdata.get_tile_image_by_gid #타일의 고유번호를 가져옴
        for layer in self.tmxdata.visible_layers: #특정수의 레이어가 타일에 있음. 땅 타일, 바닥 타일 등
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid) # gid 타일 이미지를 가져옴
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

