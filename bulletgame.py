"""
 Show how to fire bullets.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/PpdJjaiLX6A
"""
import pygame
import random
import threading

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Classes


class Bug(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # self.image = pygame.Surface([20, 20])
        # self.image.fill(RED)

        # self.rect = self.image.get_rect()
        self.image = pygame.Surface((50,50))
        self.playerx= float(screen_width/2)
        self.playery= float(screen_height/2)
        self.image.fill(RED) #플레이어 이미지 필요 
        self.rect = pygame.Rect(self.playerx, self.playery, 50,50)
        self.rect.center = (screen_width/2, screen_height/2)

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        self.rect = pygame.Rect(self.playerx, self.playery, 50,50)
        if 0< self.playerx < screen_width and 0<self.playery<screen_height:
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

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3


# --- Create the window

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# --- Sprite lists

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
bug_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# --- Create the sprites

# for i in range(50):
#     # This represents a block
#     block = Block(BLUE)

#     # Set a random location for the block
#     block.rect.x = random.randrange(screen_width)
#     block.rect.y = random.randrange(350)

#     # Add the block to the list of objects
#     block_list.add(block)
#     all_sprites_list.add(block)

# Create a red player block
player = Player()
all_sprites_list.add(player)

def bugs() :
    for i in range(2):
        bug = Bug()
        bug.rect.x = random.randrange(screen_width)
        bug.rect.y = random.randrange(screen_height)
        if bug.rect.x != player.playerx and bug.rect.y != player.playery :
            bug_list.add(bug)
            all_sprites_list.add(bug)
    threading.Timer(2, bugs).start()
bugs()


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        # elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    # --- Game logic

    # Call the update() method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a block
        bug_hit_list = pygame.sprite.spritecollide(bullet, bug_list, True)

        # For each block hit, remove the bullet and add to the score
        for bug in bug_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # --- Draw a frame

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(100)

pygame.quit()