import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

coin = pygame.image.load("CoinMain.png")
blackCoin = pygame.image.load("Black.png")
blackCoinRect = blackCoin.get_rect()
coinrect = coin.get_rect()

xValue = (0)
yValue = (0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
           
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
            xValue += coinrect.width
            if event.type == pygame.K_UP:
                xValue -= coinrect.height
                print("Up button")
            elif event.type == pygame.K_DOWN:
                xValue += coinrect.height
                
            elif event.type == pygame.K_LEFT:
                yValue -= coinrect.width

            elif event.type == pygame.K_RIGHT:
                yValue += coinrect.width

            print(xValue, yValue)
            screen.blit(coin,(xValue, yValue))
        else:
            screen.blit(blackCoin, ((xValue-36), (yValue)))
           
        
            
    pygame.display.update() 
    clock.tick(60)

pygame.quit()
quit()