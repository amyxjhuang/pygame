import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH,HEIGHT)) #height of window i guess

pygame.display.set_caption("Hello world First game")

#character
x = 50
y = 50
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < WIDTH - width:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < HEIGHT - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -5:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 5
    win.fill((0))
    pygame.draw.rect(win, (255, 200, 200), (x, y, width, height))
    pygame.display.update()

pygame.quit()
