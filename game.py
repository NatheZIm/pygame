import pygame

# 1. init
pygame.init()

# 2. setup game window
size = (600,800)
canvas = pygame.display.set_mode(size)

# 3. clock
clock = pygame.time.Clock()

# 4.1 Load image
player1_image = pygame.image.load("./player1.png").convert()
player2_image = pygame.image.load("./player1.png").convert()


player1X = 100
player1Y = 200

player2X = 200
player2Y = 200


gameloop = True
while gameloop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameloop = False

    # player 1 move 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1Y -= 5
            print(player1X,player1Y)
        if keys[pygame.K_s]:
            player1Y +=5
            print(player1X,player1Y)
        if keys[pygame.K_a]:
            player1X -=5
            print(player1X,player1Y)
        if keys[pygame.K_d]:
            player1X +=5
            print(player1X,player1Y)

    # player 2 move with keyboard
        if keys[pygame.K_UP]:
            player2Y -= 5
            print(player2X,player2Y)
        if keys[pygame.K_DOWN]:
            player2Y +=5
            print(player2X,player2Y)
        if keys[pygame.K_LEFT]:
            player2X -=5
            print(player2X,player2Y)
        if keys[pygame.K_RIGHT]:
            player2X +=5
            print(player2X,player2Y)

    # player 2 move with mouse
    # mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    # canvas.blit(player2_image, (mouse_pos))


    canvas.fill((255,0,0))
    canvas.blit(player1_image, (player1X,player1Y))
    canvas.blit(player1_image, (player2X,player2Y))
    
    clock.tick(60)
    pygame.display.flip()



