import pygame
pygame.init()

win = pygame.display.set_mode((500,480)) #height of window i guess

pygame.display.set_caption("Reese's World")
#from tutorial copy pasted
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
s1 = pygame.image.load('start1.png')
s2 = pygame.image.load('start2.png')
bg = pygame.image.load('bg.png')

char = pygame.image.load('standing.png')

#character

clock = pygame.time.Clock()
score = 0

startGame = False
startLoop = 1

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)


    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True


    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
#pygame.draw.rect(win, (255,0,0), self.hitbox,2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print('kachOW! You just HIT annie')
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():

    if startGame:
        win.blit(bg, (0,0))
    #    text = font.render("reese's cs grade: " + str(score), 1, (0,0,0))
    #     Arguments are: text, anti-aliasing, color
    #    win.blit(text, (10, 30))
        annie.draw(win)
        reese.draw(win)
        for bullet in bullets:
            bullet.draw(win)
    else:
        global startLoop
        win.blit(s1,(0,0))

        if startLoop <= 25:
            win.blit(s2, (0,0))
        startLoop = (startLoop + 1) % 50

    pygame.display.update()


reese = player(300, 385, 64, 64)
annie = enemy(100, 385, 64, 64, 450)
#annie2 = enemy(50, 385, 64, 64, 450)
shootLoop = 0

bullets = []
run = True


while run:

    clock.tick(27) #fps- frames per second

    if shootLoop > 0:
        shootLoop = (shootLoop + 1)
    if shootLoop > 3:
        shootLoop = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_TAB]:
        startGame = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < annie.hitbox[1] + annie.hitbox[3] and bullet.y + bullet.radius > annie.hitbox[1]:
            if bullet.x + bullet.radius > annie.hitbox[0] and bullet.x - bullet.radius < annie.hitbox[0] + annie.hitbox[2]:
                annie.hit()
                score += 1
                bullets.pop(bullets.index(bullet))



        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if reese.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(reese.x + reese.width//2), round(reese.y + reese.height//2), 3, (0,0,0), facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and reese.x > 0:
        reese.x -= reese.vel
        reese.left = True
        reese.right = False
        reese.standing = False
    elif keys[pygame.K_RIGHT] and reese.x < 500 - reese.width:
        reese.x += reese.vel
        reese.right = True
        reese.left = False
        reese.standing = False
    else:
        reese.standing = True
        reese.walkCount = 0

    if not reese.isJump:
        if keys[pygame.K_UP]:
            reese.isJump = True
            reese.right = False
            reese.left = False
            reese.walkCount = 0
    else:
        if reese.jumpCount >= -10:
            neg = 1
            if reese.jumpCount < 0:
                neg = -1
            reese.y -= (reese.jumpCount ** 2) * 0.5 * neg
            reese.jumpCount -= 1
        else:
            reese.isJump = False
            reese.jumpCount = 10
    redrawGameWindow()

pygame.quit()
