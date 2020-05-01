import pygame
import random
from setting import *
import time 
from time import sleep
import threading
# --- Global constants ---
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
 
# SCREEN_WIDTH = 700
# SCREEN_HEIGHT = 500
 
# --- Classes ---
 
 
class Bug(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self,x,y):
        # """ Constructor, create the image of the block. """
        super().__init__()
        mos = pygame.image.load('image/mos.png')
        img_scale_mos = pygame.transform.scale(mos,(40,40))
        self.image = img_scale_mos
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self) :
        a = random.randint(0,width)
        b = random.randint(0,height)

class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.playerx= width/2
        self.playery= height/2 
        self.image.fill(green) #플레이어 이미지 필요 
        self.rect = pygame.Rect(self.playerx, self.playery, 50,50)
        self.rect.center = (width/2, height/2)  
 
    def update(self):
        # """ Update the player location. """
        self.rect = pygame.Rect(self.playerx, self.playery, 50,50)
        key_event = pygame.key.get_pressed()
        if key_event[pygame.K_LEFT]: 
            self.playerx -= 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_LEFT]:
            self.playerx -= 2
        if key_event[pygame.K_RIGHT]:
            self.playerx += 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_RIGHT]:
            self.playerx += 2
        if key_event[pygame.K_UP]:
            self.playery -= 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_UP]:
            self.playery -= 2
        if key_event[pygame.K_DOWN]:
            self.playery += 1
        if key_event[pygame.K_LCTRL] and key_event[pygame.K_DOWN]:
            self.playery += 2
 
 
class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
 
    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """
 
        self.score = 0
        self.game_over = False
 
        # Create sprite lists
        self.bug_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
 
        # Create the block sprites
        # for i in range(10):
        #     bug = Bug()
 
        #     bug.rect.x = random.randrange(width)
        #     bug.rect.y = random.randrange(height)
 
        #     self.bug_list.add(bug)
        #     self.all_sprites_list.add(bug)
        # threading.Timer(2, self.bug).start()
        self.bugs()
 
        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)
        
    def bugs(self) :
        for i in range(2):
            a = random.randrange(width)
            b = random.randrange(height)
            bug = Bug(a, b)
            self.bug_list.add(bug)
            self.all_sprites_list.add(bug)
        threading.Timer(2, self.bugs).start()

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False
 
    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
 
            # See if the player block has collided with anything.
            bugs_hit_list = pygame.sprite.spritecollide(self.player, self.bug_list, True)
 
            # Check the list of collisions.
            for block in bugs_hit_list:
                self.score += 1
                print(self.score)
                # You can do something with "block" here.
 
            if len(self.bug_list) == 0:
                self.game_over = True
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(white)
 
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, black)
            center_x = (width // 2) - (text.get_width() // 2)
            center_y = (height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
 
        pygame.display.flip()

    # def task(self) :
    #     for i in range(3):
    #         self.bug = pygame.sprite.Group()
    #         a = random.randint(0,width)
    #         b = random.randint(0,height)
    #         bug = Bug(a, b)
    #     threading.Timer(2, self.task).start()
 
 
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [width, height]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic()
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(FPS)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()