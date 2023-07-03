import pygame 
import random
pygame.init()

#colors
white = (255,255,255)

#game window, caption, logo
SCREEN = pygame.display.set_mode((500,700))
pygame.display.set_caption("Car Game 2D")
LOGO = pygame.image.load("image/logo.png")
pygame.display.set_icon(LOGO)

#background
BG = pygame.image.load("image/bg.png")
ROAD = pygame.image.load("image/road.png")

#game specific variables
GAME_OVER = False
START_GAME = False

#lane markings
LaneY = 0
LaneY_change = 0
def Lane(LaneY):
    pygame.draw.rect(SCREEN,white,pygame.Rect(240,LaneY,20,80))
    pygame.draw.rect(SCREEN,white,pygame.Rect(240,LaneY+120,20,80))
    pygame.draw.rect(SCREEN,white,pygame.Rect(240,LaneY+240,20,80))
    pygame.draw.rect(SCREEN,white,pygame.Rect(240,LaneY+360,20,80))
    pygame.draw.rect(SCREEN,white,pygame.Rect(240,LaneY+480,20,80))
    pygame.draw.rect(SCREEN,white,pygame.Rect(240,LaneY+590,20,80))

#start ui
START = pygame.image.load("image/start.png")
clock = pygame.time.Clock()
count = 3
COUNT = True
font = pygame.font.Font(None,130)
pygame.time.set_timer(COUNT, 1000)

#player car
playerImg = pygame.image.load("image/car1.png")
playerX = 190
playerY = 570
playerX_change = 0
playerY_change = 0
def player(x,y):
    SCREEN.blit(playerImg,(x,y))

#coin
coinImgs = []
coinX1 = []
coinX2 = []
coinX3 = []
coinY1 = 0
coinY2 = 50
coinY3 = 100
for i in range(2):
    coinImgs.append(pygame.image.load("image/coin.png"))
    coinX1.append(random.randint(120,340))
    coinX2.append(random.randint(120,340))
    coinX3.append(random.randint(120,340))

#game loop
while not GAME_OVER:
    if not START_GAME :
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(ROAD,(100,0))
        SCREEN.blit(START,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER =True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                START_GAME = True
            if event.key == pygame.K_UP:
                playerY_change = 3
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_LEFT:
                playerX_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
                    
    if START_GAME:
        if COUNT:
            clock.tick(2)
            countText = font.render(str(count),True, white)
            count -= 1
            SCREEN.blit(BG,(0,0))
            SCREEN.blit(ROAD,(100,0))
            SCREEN.blit(countText,(230,280))
            if count == 0:
                pygame.time.set_timer(COUNT, 0) 
                COUNT = False
        else:
            if count == 0:
                clock.tick(2)
                count += 1
            else:
                SCREEN.blit(BG,(0,0))
                SCREEN.blit(ROAD,(100,0))
                #when the player y axis is equal to 570 do not start the lane movement 
                if playerY == 570:
                    Lane(LaneY)
                #when the player y axis greater than 570 start the lane movement 
                else:
                    LaneY_change = 5
                    LaneY += LaneY_change
                    Lane(LaneY)
                    #coin generating part
                    if coinY1 >=0 and coinY1<=700:
                        coinY1 = coinY1+3
                        for i in range (2):
                            SCREEN.blit(coinImgs[i],(coinX1[i],coinY1))
                    else:
                        coinY1 = 0
                    if coinY2 >=50 and coinY2<=700:
                        coinY2 = coinY2+3
                        for i in range (2):
                            SCREEN.blit(coinImgs[i],(coinX2[i],coinY2))
                    else:
                        coinY2 = 50
                    if coinY3 >=100 and coinY3<=700:
                        coinY3 = coinY3+3
                        for i in range (2):
                            SCREEN.blit(coinImgs[i],(coinX3[i],coinY3))
                    else:
                        coinY3 = 100
                    
                #when the 1st lane is equal to the secont lane y axis, iterate the lane movement
                if LaneY == 120:
                    LaneY = 0
                #when player y axis is equal to 350, stop the futher movement of the player
                if playerY <350:
                    playerY_change = 0
                else:
                    playerY -= playerY_change
                playerX +=playerX_change
                if playerX <=100:
                    playerX = 100
                if playerX >=270:
                    playerX = 270
                player(playerX,playerY)
    pygame.display.update()