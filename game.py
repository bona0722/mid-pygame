
import os
import pygame
import random
from setting import *
from Entity import *
import time 
from time import sleep
import threading

class Game :
    def __init__(self) :
        self.score = 0
        self.game_over = False
        self.enemys = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(10) :
            bug = Enemy()

            bug.pos()

            self.enemys.add(bug)
            self.all_sprites_list.add(bug)
        self.player = Player()
        self.all_sprites_list.add(self.player)


    def run_logic(self) :
        if not self.game_over:
            self.all_sprites_list.update()
            enemys_hit_list = pygame.sprite.pygame.sprite.spritecollide(self.player, self.enemys, True)

            for bug in enemys_hit_list :
                self.score += 100
                print(self.score)

            if len(self.enemys) == 0:
                self.game_over = True
        
    # def bugmaking(self) :
    #     a = random.randint(0,width)
    #     b = random.randint(0,height)
    #     bug = Enemy(a, b)
    #     threading.Timer(2.5,self.bugmaking).start()

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bug Game")
    
    clock = pygame.time.Clock()
    run = True
    game = Game()

    while run :
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__" :
    main()



