import pygame
import random
import math
import time

from pygame import mixer # sound

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Comic Sans MS", 30)

# Background
background = pygame.image.load("chinese background.jpg")

# Game name and game icon
pygame.display.set_caption('Troll fighter')
icon = pygame.image.load('kung-fu.png')
pygame.display.set_icon(icon)

# player code
player_ima = pygame.image.load('kung-fu.png') # player image
playerX = 100 # player coordinates(x)
playerY = 300 # player coordinates(y)
player_change_X = 0
player_change_Y = 0

# player weapon(fireball)
fireball_ima = pygame.image.load('fireball.png')
fireball_X = playerX
fireball_Y = playerY
fireballchange_Y = 0
fireball_change_X = 2
fireball_state = 'Ready'

# enemy code(trolls)
trollImg = pygame.image.load('trolls.png')
trollSmall = []

trollX = []
trollY = []
trollSpeed = []
lives = 10

def player(x, y):
    screen.blit(player_ima, (x, y))

def fireball(x, y):
    global fireball_state
    fireball_state = 'Fire'
    screen.blit(fireball_ima, (fireball_X, fireball_Y))

for i in range(50):
    trollSmall.append(pygame.transform.scale(trollImg, (48, 64)))
    trollX.append(random.randint(800, 15000))
    trollY.append(random.randint(0, 536))
    trollSpeed.append(2)

def troll(x, y, z):
    screen.blit(trollSmall[z], (x, y))

def iscollision(trollX, trollY, fireball_X, fireball_Y):
    distance = math.sqrt(math.pow(trollX - fireball_X, 2) + math.pow(trollY -fireball_Y, 2))
    if distance < 30:
        return True
    else:
        return False
    
running = True
while running:
    screen.fill((16, 81, 179))
# background ( to make sure the image stays)
    screen.blit(background, (0, 0))
    for events in pygame.event.get():
        if (events.type == pygame.QUIT):
            running = False

        if (events.type == pygame.KEYDOWN):
            if (events.key == pygame.K_UP):
                player_change_Y += -4
            elif (events.key == pygame.K_DOWN):
                player_change_Y += 4
            elif (events.key == pygame.K_SPACE):

                fireball_X = playerX
                fireball_Y = playerY
                fireball(fireball_X, fireball_Y)
                fireball_sound = mixer.Sound('shoot.wav')
                fireball_sound.play()
            elif events.type == pygame.KEYUP:
                if events.key == events.key == pygame.K_UP or events.key ==pygame.K_DOWN:
                    player_change_Y = 0
                    playerY += player_change_Y

# enemy(troll) movement
    for i in range(50):
        troll(trollX[i], trollY[i], i)
        if trollX[i] <= 0:
            trollX[i] = random.randint(800, 2000)
            lives -= 1
            print(lives)
        else:
            trollX[i] -= trollSpeed[i]

    # colllisions
        collision = iscollision(trollX[i], trollY[i], fireball_X, fireball_Y)
        if collision:
            fireball_state = 'Ready'
            fireball_X = playerX
            fireball_Y = playerY
            trollX[i] = random.randint(800, 2000)
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()

# fireball movement
    if fireball_state == "Fire":
        fireball_X += 4
        fireball(fireball_X, fireball_Y)
    if playerY >= 568:
        playerY = 568
    elif playerY < 0:
        playerY = 0

    player(playerX, playerY)
    textSurface = font.render('Lives:' + str(lives), False, (255, 255, 255))
    screen.blit(textSurface, (650, 25))

    if lives <= 0:
        gameOver = font.render('Game Over!', False, (255, 255, 255))
        screen.blit(gameOver, (290, 290))

        time.sleep(3)
        running = False

    pygame.display.update()