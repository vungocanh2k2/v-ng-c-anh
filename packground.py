import pygame

pygame.init()


#screen,backgroud

width =1102
height = 620
screen = pygame.display.set_mode((width,height))
background_img = pygame.image.load(r'C:\Users\Vu Ngoc Anh\Pictures\Screenshots\packgroudzombie.jpg') 
icon = pygame.image.load(r'C:\Users\Vu Ngoc Anh\Pictures\Screenshots\soldier1.png')
pygame.display.set_caption("The Last Survival")
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\soldier.png")
playerX = 551
playerY = 510
playerZ = 0


#zoombies
zoombies_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\zombie.png")
zombieX = 360
zombieY = 0

#barrier
barrier1_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\barrier.png")
barrier1x = 450
barrier1y = 400
barrier2_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\barrier.png")
barrier2x = 517
barrier2y = 400
barrier3_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\barrier.png")
barrier3x = 585
barrier3y = 400

#wall
wall1_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\wall.png")
wall1x = 250
wall1y = 450
wall2_img =  pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\wall.png")
wall2x = 250
wall2y = 500
wall3_img =  pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\wall.png")
wall3x = 800
wall3y = 450
wall4_img =  pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\wall.png")
wall4x = 800
wall4y = 500
#pickwall
pickwall1_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall1x = 100
pickwall1y = 350
pickwall2_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall2x = 200
pickwall2y = 100
pickwall3_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall3x = 350
pickwall3y = 250
pickwall4_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall4x = 550
pickwall4y = 100
pickwall5_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall5x = 700
pickwall5y = 250
pickwall6_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall6x = 900
pickwall6y = 100
pickwall7_img = pygame.image.load(r"C:\Users\Vu Ngoc Anh\Pictures\Screenshots\bickwall.png")
pickwall7x = 1000
pickwall7y = 350



















running = True
while running:
    #icon position 
    screen.blit(background_img,(0, 0))
    screen.blit(player_img,(playerX,playerY))
    screen.blit(zoombies_img,(zombieX,zombieY))
    screen.blit(barrier1_img,(barrier1x,barrier1y))
    screen.blit(barrier2_img,(barrier2x,barrier2y))
    screen.blit(barrier3_img,(barrier3x,barrier3y))
    screen.blit(wall1_img,(wall1x,wall1y))
    screen.blit(wall2_img,(wall2x,wall2y))
    screen.blit(wall3_img,(wall3x,wall3y))
    screen.blit(wall4_img,(wall4x,wall4y))
    screen.blit(pickwall1_img,(pickwall1x,pickwall1y))
    screen.blit(pickwall2_img,(pickwall2x,pickwall2y))
    screen.blit(pickwall3_img,(pickwall3x,pickwall3y))
    screen.blit(pickwall4_img,(pickwall4x,pickwall4y))
    screen.blit(pickwall5_img,(pickwall5x,pickwall5y))
    screen.blit(pickwall6_img,(pickwall6x,pickwall6y))
    screen.blit(pickwall7_img,(pickwall7x,pickwall7y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#key setting
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 0.4
        if event.key == pygame.K_RIGHT:
            playerX += 0.4
        if event.key == pygame.K_UP:
            playerY -= 0.4
        if event.key == pygame.K_DOWN:
            playerY += 0.4
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT == pygame.K_RIGHT == pygame.K_UP == pygame.K_DOWN:
            playerZ = 0
#
    if playerY  <= 400 :
        playerY  = 400
    elif playerY >= 550:
        playerY = 550
    elif playerX <=250:
        playerX = 250
    elif playerX >= 900:
        playerX = 900
    playerY += playerZ
    pygame.display.update()