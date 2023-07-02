import pygame 
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
                
    if START_GAME:
        if COUNT:
            clock.tick(1)
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
                clock.tick(1)
                count += 1
            else:
                SCREEN.blit(BG,(0,0))
                SCREEN.blit(ROAD,(100,0))
                LaneY_change = 5
                LaneY += LaneY_change
                Lane(LaneY)
                if LaneY == 120:
                    LaneY = 0
    pygame.display.update()