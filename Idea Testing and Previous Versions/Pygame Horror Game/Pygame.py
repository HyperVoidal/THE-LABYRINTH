import pygame
import time as t
# pygame setup
pygame.init()
pygame.font.init()
world = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()
global mazewincount
mazewincount = 0
running = True
playerx = 120
playery = 480
iconx = playerx
icony = playery
enemyx = 400
enemyy = 10
bg = pygame.image.load("maze.png")
background = pygame.transform.scale(bg, (835, 835))
monstimg = pygame.image.load("monster.png")
monster = pygame.transform.scale(monstimg, (30, 30))
imga = pygame.image.load("Hero.png")
img = pygame.transform.scale(imga, (25, 25))
bg1 = 55
bg2 = 55
bg3 = 55


def pursuer():
    pursimg = pygame.image.load("monster.png") #Put path for monster png here
    pursuer = pygame.draw.rect(world, (bg1, bg2, bg3), (enemyx, enemyy, 30, 30))
    

    
def endgame(mazewincount):
    mazewincount += 1
    for i in range(20):
        world.fill((15 + (i * 12), 15 + (i * 12), 15 + (i * 12)))
        pygame.display.flip()
        t.sleep(0.05)
        
def wallcaller():
    pygame.draw.rect(world, (0, 0, 0), rect2)
    pygame.draw.rect(world, (0, 0, 0), rect3)
    pygame.draw.rect(world, (0, 0, 0), rect4)
    pygame.draw.rect(world, (0, 0, 0), rect5)
    pygame.draw.rect(world, (0, 0, 0), rect6)
    pygame.draw.rect(world, (0, 0, 0), rect7)
    pygame.draw.rect(world, (0, 0, 0), rect8)
    pygame.draw.rect(world, (0, 0, 0), rect9)
    pygame.draw.rect(world, (0, 0, 0), rect10)
    pygame.draw.rect(world, (0, 0, 0), rect11)
    pygame.draw.rect(world, (0, 0, 0), rect12)
    pygame.draw.rect(world, (0, 0, 0), rect13)
    pygame.draw.rect(world, (0, 0, 0), rect14)
    pygame.draw.rect(world, (0, 0, 0), rect15)
    pygame.draw.rect(world, (0, 0, 0), rect16)
    pygame.draw.rect(world, (0, 0, 0), rect17)
    pygame.draw.rect(world, (0, 0, 0), rect18)
    pygame.draw.rect(world, (0, 0, 0), rect19)
    pygame.draw.rect(world, (0, 0, 0), rect20)
    pygame.draw.rect(world, (0, 0, 0), rect21)
    pygame.draw.rect(world, (0, 0, 0), rect22)
    pygame.draw.rect(world, (0, 0, 0), rect23)
    pygame.draw.rect(world, (0, 0, 0), rect24)
    pygame.draw.rect(world, (0, 0, 0), rect25)
    pygame.draw.rect(world, (0, 0, 0), rect26)
    pygame.draw.rect(world, (0, 0, 0), rect27)
    pygame.draw.rect(world, (0, 0, 0), rect28)
    pygame.draw.rect(world, (0, 0, 0), rect29)
    pygame.draw.rect(world, (0, 0, 0), rect30)
    pygame.draw.rect(world, (0, 0, 0), rect31)
    pygame.draw.rect(world, (0, 0, 0), rect32)
    pygame.draw.rect(world, (0, 0, 0), rect33)
    pygame.draw.rect(world, (0, 0, 0), rect34)
    pygame.draw.rect(world, (0, 0, 0), rect35)
    pygame.draw.rect(world, (0, 0, 0), rect36)
    pygame.draw.rect(world, (0, 0, 0), rect37)
    pygame.draw.rect(world, (0, 0, 0), rect38)
    pygame.draw.rect(world, (0, 0, 0), rect39)
    pygame.draw.rect(world, (0, 0, 0), rect40)
    pygame.draw.rect(world, (0, 0, 0), rect41)
    pygame.draw.rect(world, (0, 0, 0), rect42)
    pygame.draw.rect(world, (0, 0, 0), rect43)
    pygame.draw.rect(world, (0, 0, 0), rect44)
    pygame.draw.rect(world, (0, 0, 0), rect45)
    pygame.draw.rect(world, (0, 0, 0), rect46)
    pygame.draw.rect(world, (0, 0, 0), rect47)
    pygame.draw.rect(world, (0, 0, 0), rect48)
    pygame.draw.rect(world, (0, 0, 0), rect49)
    pygame.draw.rect(world, (0, 0, 0), rect50)
    pygame.draw.rect(world, (0, 0, 0), rect51)
    pygame.draw.rect(world, (0, 0, 0), rect52)
    pygame.draw.rect(world, (0, 0, 0), rect53)
    pygame.draw.rect(world, (0, 0, 0), rect54)
    pygame.draw.rect(world, (0, 0, 0), rect55)
    pygame.draw.rect(world, (0, 0, 0), rect56)
    pygame.draw.rect(world, (0, 0, 0), rect57)
    pygame.draw.rect(world, (0, 0, 0), rect58)
    pygame.draw.rect(world, (0, 0, 0), rect59)
    pygame.draw.rect(world, (0, 0, 0), rect60)
    pygame.draw.rect(world, (0, 0, 0), rect61)
    pygame.draw.rect(world, (0, 0, 0), rect62)
    pygame.draw.rect(world, (0, 0, 0), rect63)
    pygame.draw.rect(world, (0, 0, 0), rect64)
    pygame.draw.rect(world, (0, 0, 0), rect65)
    pygame.draw.rect(world, (0, 0, 0), rect66)
    pygame.draw.rect(world, (0, 0, 0), rect67)
    pygame.draw.rect(world, (0, 0, 0), rect68)
    pygame.draw.rect(world, (0, 0, 0), rect69)
    pygame.draw.rect(world, (0, 0, 0), rect70)
    pygame.draw.rect(world, (0, 0, 0), rect71)
    pygame.draw.rect(world, (0, 0, 0), rect72)
    pygame.draw.rect(world, (0, 0, 0), rect73)
    pygame.draw.rect(world, (0, 0, 0), rect74)
    pygame.draw.rect(world, (0, 0, 0), rect75)
    pygame.draw.rect(world, (0, 0, 0), rect76)
    pygame.draw.rect(world, (0, 0, 0), rect77)
    pygame.draw.rect(world, (0, 0, 0), rect78)
    pygame.draw.rect(world, (0, 0, 0), rect79)
    pygame.draw.rect(world, (0, 0, 0), rect80)
    pygame.draw.rect(world, (0, 0, 0), rect81)
    pygame.draw.rect(world, (0, 0, 0), rect82)
    pygame.draw.rect(world, (0, 0, 0), rect83)
    pygame.draw.rect(world, (0, 0, 0), rect84)
    pygame.draw.rect(world, (0, 0, 0), rect85)
    pygame.draw.rect(world, (0, 0, 0), rect86)
    pygame.draw.rect(world, (0, 0, 0), rect87)
    pygame.draw.rect(world, (0, 0, 0), rect88)
    pygame.draw.rect(world, (0, 0, 0), rect89)
    pygame.draw.rect(world, (0, 0, 0), rect90)
    pygame.draw.rect(world, (0, 0, 0), rect91)
    pygame.draw.rect(world, (0, 0, 0), rect92)
    pygame.draw.rect(world, (0, 0, 0), rect93)
    pygame.draw.rect(world, (0, 0, 0), rect94)
    pygame.draw.rect(world, (0, 0, 0), rect95)

def collisioncaller():
    if rect1.colliderect(rect2) or rect1.colliderect(rect3) or rect1.colliderect(rect4) or rect1.colliderect(rect5) or rect1.colliderect(rect6) or rect1.colliderect(rect7) or rect1.colliderect(rect8) or rect1.colliderect(rect9) or rect1.colliderect(rect10):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect11) or rect1.colliderect(rect12) or rect1.colliderect(rect13) or rect1.colliderect(rect14) or rect1.colliderect(rect15) or rect1.colliderect(rect16) or rect1.colliderect(rect17) or rect1.colliderect(rect18) or rect1.colliderect(rect19):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect20) or rect1.colliderect(rect21) or rect1.colliderect(rect22) or rect1.colliderect(rect23) or rect1.colliderect(rect24) or rect1.colliderect(rect25) or rect1.colliderect(rect26) or rect1.colliderect(rect27) or rect1.colliderect(rect28) or rect1.colliderect(rect29) or rect1.colliderect(rect30):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect31) or rect1.colliderect(rect32) or rect1.colliderect(rect33) or rect1.colliderect(rect34) or rect1.colliderect(rect35) or rect1.colliderect(rect36) or rect1.colliderect(rect37) or rect1.colliderect(rect38) or rect1.colliderect(rect39) or rect1.colliderect(rect40):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect41) or rect1.colliderect(rect42) or rect1.colliderect(rect43) or rect1.colliderect(rect44) or rect1.colliderect(rect45) or rect1.colliderect(rect46) or rect1.colliderect(rect47) or rect1.colliderect(rect48) or rect1.colliderect(rect49) or rect1.colliderect(rect50):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect51) or rect1.colliderect(rect52) or rect1.colliderect(rect53) or rect1.colliderect(rect54) or rect1.colliderect(rect55) or rect1.colliderect(rect56) or rect1.colliderect(rect57) or rect1.colliderect(rect58) or rect1.colliderect(rect59) or rect1.colliderect(rect60):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect61) or rect1.colliderect(rect62) or rect1.colliderect(rect63) or rect1.colliderect(rect64) or rect1.colliderect(rect65) or rect1.colliderect(rect66) or rect1.colliderect(rect67) or rect1.colliderect(rect68) or rect1.colliderect(rect69) or rect1.colliderect(rect70):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect71) or rect1.colliderect(rect72) or rect1.colliderect(rect73) or rect1.colliderect(rect74) or rect1.colliderect(rect75) or rect1.colliderect(rect76) or rect1.colliderect(rect77) or rect1.colliderect(rect78) or rect1.colliderect(rect79) or rect1.colliderect(rect80):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect81) or rect1.colliderect(rect82) or rect1.colliderect(rect83) or rect1.colliderect(rect84) or rect1.colliderect(rect85) or rect1.colliderect(rect86) or rect1.colliderect(rect87) or rect1.colliderect(rect88) or rect1.colliderect(rect89) or rect1.colliderect(rect90):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y
    if rect1.colliderect(rect91) or rect1.colliderect(rect92) or rect1.colliderect(rect93) or rect1.colliderect(rect94) or rect1.colliderect(rect95):
        rect1.x = previous_x
        rect1.y = previous_y
        playerx = rect1.x
        playery = rect1.y

#Maze Collision
rect1 = pygame.Rect(759, 250, 20, 20)
rect2 = pygame.Rect(0, 0, 20, 800)
rect3 = pygame.Rect(0, 0, 1000, 12)
rect4 = pygame.Rect(788, 0, 20, 1000)
rect5 = pygame.Rect(0, 788, 1000, 12)
rect6 = pygame.Rect(728, 360, 60, 20)
rect7 = pygame.Rect(728, 255, 20, 110)
rect8 = pygame.Rect(678, 150, 100, 20)
rect9 = pygame.Rect(730, 150, 20, 50)
rect10 = pygame.Rect(620, 200, 120, 20)
rect11 = pygame.Rect(628, 255, 120, 20)
rect12 = pygame.Rect(623, 100, 20, 100)
rect13 = pygame.Rect(573, 100, 60, 20)
rect14 = pygame.Rect(572, 120, 20, 205)
rect15 = pygame.Rect(623, 275, 20, 55)
rect16 = pygame.Rect(676, 315, 20, 50)
rect17 = pygame.Rect(570, 358, 105, 20)
rect18 = pygame.Rect(208, 255, 360, 20)
rect19 = pygame.Rect(462, 277, 20, 40)
rect20 = pygame.Rect(515, 310, 20, 100)
rect21 = pygame.Rect(311, 310, 210, 20)
rect22 = pygame.Rect(518, 412, 48, 20)
rect23 = pygame.Rect(573, 379, 20, 55)
rect24 = pygame.Rect(625, 412, 120, 20)
rect25 = pygame.Rect(728, 412, 20, 180)
rect26 = pygame.Rect(593, 466, 98, 20)
rect27 = pygame.Rect(671, 476, 20, 280) 
rect28 = pygame.Rect(572, 727, 100, 20)
rect29 = pygame.Rect(572, 529, 20, 200)
rect30 = pygame.Rect(725, 622, 20, 120)
rect31 = pygame.Rect(725, 622, 100, 20)
rect32 = pygame.Rect(515, 679, 20, 70)
rect33 = pygame.Rect(410, 673, 100, 20)
rect34 = pygame.Rect(464, 694, 20, 70)
rect35 = pygame.Rect(470, 625, 100, 20)
rect36 = pygame.Rect(362, 517, 70, 20)
rect37 = pygame.Rect(410, 538, 20, 200)
rect38 = pygame.Rect(464, 466, 20, 120)
rect39 = pygame.Rect(485, 466, 100, 20)
rect40 = pygame.Rect(520, 517, 50, 20)
rect41 = pygame.Rect(520, 517, 20, 70)
rect42 = pygame.Rect(362, 412, 100, 20)
rect43 = pygame.Rect(362, 361, 20, 60)
rect44 = pygame.Rect(255, 362, 95, 20)
rect45 = pygame.Rect(254, 382, 20, 70)
rect46 = pygame.Rect(275, 412, 30, 20)
rect47 = pygame.Rect(310, 412, 20, 100)
rect48 = pygame.Rect(326, 465, 100, 20)
rect49 = pygame.Rect(362, 724, 60, 20)
rect50 = pygame.Rect(362, 571, 20, 150)
rect51 = pygame.Rect(308, 575, 20, 110)
rect52 = pygame.Rect(254, 673, 60, 20)
rect53 = pygame.Rect(257, 516, 20, 140)
rect54 = pygame.Rect(293, 517, 30, 20)
rect55 = pygame.Rect(158, 466, 100, 20)
rect56 = pygame.Rect(205, 466, 20, 230)
rect57 = pygame.Rect(260, 463, 20, 20)
rect58 = pygame.Rect(308, 724, 20, 60)
rect59 = pygame.Rect(152, 724, 150, 20)
rect60 = pygame.Rect(149, 630, 20, 110)
rect61 = pygame.Rect(50, 568, 150, 20)
rect62 = pygame.Rect(47, 467, 20, 100)
rect63 = pygame.Rect(47, 619, 120, 20)
rect64 = pygame.Rect(47, 619, 20, 100)
rect65 = pygame.Rect(47, 728, 75, 20)
rect66 = pygame.Rect(100, 680, 20, 50)
rect67 = pygame.Rect(149, 487, 20, 50)
rect68 = pygame.Rect(95, 511, 55, 20)
rect69 = pygame.Rect(95, 315, 20, 200)
rect70 = pygame.Rect(46, 310, 50, 20)
rect71 = pygame.Rect(46, 310, 20, 60)
rect72 = pygame.Rect(48, 415, 60, 20)
rect73 = pygame.Rect(20, 253, 50, 20)
rect74 = pygame.Rect(48, 204, 20, 50)
rect75 = pygame.Rect(98, 154, 20, 100)
rect76 = pygame.Rect(20, 154, 100, 20)
rect77 = pygame.Rect(464, 361, 20, 80)
rect78 = pygame.Rect(415, 361, 60, 20)
rect79 = pygame.Rect(203, 312, 70, 20)
rect80 = pygame.Rect(203, 312, 20, 100)
rect81 = pygame.Rect(150, 412, 70, 20)
rect82 = pygame.Rect(150, 110, 20, 300)
rect83 = pygame.Rect(47, 97, 120, 20)
rect84 = pygame.Rect(47, 49, 20, 60)
rect85 = pygame.Rect(47, 44, 280, 27)
rect86 = pygame.Rect(306, 73, 20, 80)
rect87 = pygame.Rect(204, 148, 125, 20)
rect88 = pygame.Rect(201, 100, 70, 20)
rect89 = pygame.Rect(201, 100, 20, 130)
rect90 = pygame.Rect(174, 202, 30, 30)
rect91 = pygame.Rect(621, 487, 20, 100)
rect92 = pygame.Rect(621, 619, 20, 70)
rect93 = pygame.Rect(621, 619, 50, 20)
rect94 = pygame.Rect(357, 13, 28, 250)
rect95 = pygame.Rect(257, 205, 100, 20)

previous_x, previous_y = 0, 0
x_change, y_change = 0, 0

speed = 3
collcounter = 2
counter = 0
wincount = 0
keyremoval = 0
while running:
    if counter % 2 != 0:
        t.sleep(2)
        counter += 1
        
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -speed
                y_change = 0
            if event.key == pygame.K_d:
                x_change = speed
                y_change = 0
            if event.key == pygame.K_s:
                y_change = speed
                x_change = 0
            if event.key == pygame.K_w:
                y_change = -speed
                x_change = 0
            if event.key == pygame.K_p:
                print("x = " + str(rect1.x) + " y = " + str(rect1.y))
            if event.key == pygame.K_BACKSPACE:
                collcounter += 1

        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 0

    world.fill((bg1, bg2, bg3))

    pursuer()
    previous_x = rect1.x
    previous_y = rect1.y

    rect1.x = rect1.x + x_change
    rect1.y = rect1.y + y_change
    playerx = rect1.x
    playery = rect1.y
    if collcounter % 2 == 0:
        collisioncaller()
        wallcaller()
    else:
        collcounter += 0
    pygame.draw.rect(world, (0, 255, 0), (150, 780, 100, 60))
    
    pygame.draw.rect(world, (bg1, bg2, bg3), rect1, 1)
    
    #Key and Door Rendering
    if wincount == 1:
        #Key blitting
        key1rect = pygame.Rect(20, 225, 20, 20)
        pygame.draw.rect(world, (bg1, bg2, bg3), key1rect)
        keyimg = pygame.image.load("Gold Key.png")
        key1 = pygame.transform.rotate(keyimg, (90))
        key = pygame.transform.scale(key1, (20, 30))
        world.blit(key, (key1rect.x, key1rect.y))
        if rect1.colliderect(key1rect):
            keyremoval += 1
        door1rect = pygame.Rect(0, 0, 0, 0)
        pygame.draw.rect(world, (bg1, bg2, bg3), door1rect)
        
    
    #Key collision
    if keyremoval > 0:
        key1rect.x = 900
        key1rect.y = 900
        pygame.draw.rect(world, (bg1, bg2, bg3), (20, 225, 20, 30))
            
            
        

    world.blit(img, (playerx, playery))
    world.blit(background, ((-20), (-20)))
    world.blit(monster, (enemyx, enemyy))
    if rect1.colliderect((150, 780, 100, 60)):
        endgame(mazewincount)
        world.fill((55, 55, 55))
        rect1.x = 759
        rect1.y = 250
        wincount += 1
        if wincount == 1:
            font = pygame.font.SysFont('Adagio Sans', 75)
            fontsmaller = pygame.font.SysFont('Adagio Sans', 45)
            world.blit((font.render('Adventurer. Turn back now.', False, (0, 0, 0))), (25, 200))
            world.blit((fontsmaller.render('I will not let you leave this place.', False, (0, 0, 0))), (25, 300))
            pygame.display.flip()
            counter += 1

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()