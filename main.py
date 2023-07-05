import pygame 
import random
from pygame import mixer
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
mixer.music.load("audio/bg.mp3")

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
coinImg = pygame.image.load("image/coin.png")
coinX1 = random.randint(120,350)
coinX2 = random.randint(180,350)
coinX3 = random.randint(200,350)
coinY1 = 0
coinY2 = 50
coinY3 = 100
cAudio = mixer.Sound("audio/coin.wav")

#score board
sb = 0
scoreFont = pygame.font.Font(None,30)
def score(sb):
    s = scoreFont.render("Score: "+str(sb),True,white)
    SCREEN.blit(s,(5,10))
data = open("highScore.txt","r")
hsb = data.read()
def highscore(hsb,sb):
    if sb >int(hsb):
        data = open("highScore.txt","w")
        hsb = data.write(str(sb))
        s = scoreFont.render("High Score: "+str(sb),True,white)
        SCREEN.blit(s,(5,50))
    else:
        s = scoreFont.render("High Score: "+str(hsb),True,white)
        SCREEN.blit(s,(5,50))

#life 
lifeImg = "image/heart.png"
lifeX = [410,440,470]
lifeY = 10
lifeNo = 3
countl = 0
def life(i,x,y):
    SCREEN.blit(pygame.image.load(lifeImg),(x,y))

#enemy player
enemyImg = pygame.image.load("image/car2.png")
enemyX1 = random.randint(120,290)
enemyY1 = -50
enemyX2 = random.randint(120,290)
enemyY2 = 50
eAudio = mixer.Sound("audio/crash.wav")

#end ui

#game loop
while not GAME_OVER:
    if not START_GAME :
        mixer.music.play(-1) 
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
                playerX_change = 3
            if event.key == pygame.K_LEFT:
                playerX_change = -3
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
                    LaneY_change = 6
                    LaneY += LaneY_change
                    Lane(LaneY)
                    #coin generating part
                    #coin 1
                    if coinY1 >=0 and coinY1<=700:
                        coinY1 = coinY1+4
                        SCREEN.blit(coinImg,(coinX1,coinY1))
                    else:
                        coinY1 = 0
                        coinX1 = random.randint(120,350)
                    #collision
                    if coinX1>playerX-10 and coinX1<playerX+88 and coinY1>playerY-10 and coinY1<playerY+88:
                        cAudio.play()
                        coinY1 = -50 
                        coinX1 = random.randint(120,350)
                        sb = sb  + 1
                    #coin 2
                    if coinY2 >=50 and coinY2<=700:
                        coinY2 = coinY2+4
                        SCREEN.blit(coinImg,(coinX2,coinY2))
                    else:
                        coinY2 = 50
                        coinX2 = random.randint(180,350)
                    #collision
                    if coinX2>playerX-10 and coinX2<playerX+88 and coinY2>playerY-10 and coinY2<playerY+88:
                        cAudio.play()
                        coinY2 = -50 
                        coinX2 = random.randint(180,350)
                        sb = sb  + 1
                    #coin 3
                    if coinY3 >=100 and coinY3<=700:
                        coinY3 = coinY3+4
                        SCREEN.blit(coinImg,(coinX3,coinY3))
                    else:
                        coinY3 = 100   
                        coinX3 = random.randint(200,350)
                    #collision
                    if coinX3>playerX-10 and coinX3<playerX+88 and coinY3>playerY-10 and coinY3<playerY+88:
                        cAudio.play()
                        coinY3 = -50 
                        coinX3 = random.randint(200,350)
                        sb = sb  + 1
                    score(sb)
                    highscore(hsb,sb)
                    #enemy player
                    if enemyY1 >= -50 and enemyY1<=700:
                        enemyY1 = enemyY1+4
                        SCREEN.blit(enemyImg,(enemyX1,enemyY1))
                    else:
                        enemyY1 = -50  
                        enemyX1 = random.randint(120,290)
                    #collision
                    if enemyX1>=playerX-70 and enemyX1<=playerX+70 and enemyY1>=playerY-70 and enemyY1<playerY+70:
                        eAudio.play()
                        enemyY1 = 0
                        enemyX1 = random.randint(120,290)
                        lifeNo -= 1
                        #when 3 lifes are dead then game over, reset everything
                        if lifeNo == 0:
                            START_GAME =False
                            sb = 0
                            lifeNo = 3
                    for i in range (lifeNo):
                        life(i,lifeX[i],lifeY)
                    
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