import random
import pygame
import math
from pygame import mixer
pygame.init()
pygame.font.init()

icon = pygame.image.load("mitskotakis.png")

screen = pygame.display.set_mode((1000, 600))
backround = pygame.image.load("vouli_adeia_edrana_94.png")
#sound
mixer.music.load("anthem.wav")
mixer.music.play(-1)
flag = 0
# title & icon
pygame.display.set_caption("Mitso_Kill")

pygame.display.set_icon(icon)


#SCORE AND LIVES
kills =0
lives = 4

font = pygame.font.Font(None , 32 )
font2 = pygame.font.Font(None , 32)

def showscore(x,y):
    score = font.render("KILLS AGAINST BASTARDS : "+str(kills),True,(147,49,38))
    live = font2.render("LIVES: "+ str(lives) , True , (147,49,38))
    screen.blit(score,(x,y))
    screen.blit(live,(x,y+30))

# player
FoudasImg = pygame.image.load("Foudas.png")
FoudasX = 500
FoudasY = 300
incX = 0
incY = 0


def Player(FoudasImg, x, y):
    screen.blit(FoudasImg, (x, y))


# bullet
BulletImg = pygame.image.load("bullet.png")
BullX = FoudasX
BullY = F

def fire(x, y):
    global BullState
    BullState = "fire"
    screen.blit(BulletImg, (x, y))



# mitsotakis
MitImg = pygame.image.load("mitskotakis.png")
MitX = random.randint(0, 1000)
MitY = random.randint(0, 600)
M_incX = 0
M_incY = 0
def Mit(MitX, MitY):
    screen.blit(MitImg, (MitX, MitY))

#matas
MatImg = pygame.image.load("mat.png")
MatX = random.randint(0, 1000)
MatY = random.randint(0, 600)
Mat_incX = 0
Mat_incY = 0
def Mat(MatX, MatY):
    screen.blit(MatImg, (MatX, MatY))

#colision
def iscolision(MitX,MitY,BullX,BullY,value):
    distance = math.sqrt( (math.pow((BullX - MitX),2)) + (math.pow((BullY - MitY),2)))
    if distance < value :
        return True
    else :
        return False


def quiting():
    mixer.music.load("quit.wav")
    quitsound = mixer.Sound("quit.wav")
    quitsound.play()

flagover = 0



# Game loop

running = True

while running:
    if lives == 0:
        quiting()
        flagover =1

    screen.fill((0, 0, 0))
    screen.blit(backround, (0, 0))
    showscore(10,10)
    if kills % 20 == 0 and kills != 0 :
        taff = mixer.Sound("exw xasei ta logika moy .wav")
        taff.play()

    # chaseeeee
    if (MitX != FoudasX or MitY != FoudasY):
        taxitita = 0.25
        if flagover == 1:
            taxitita=0

        if FoudasX > MitX:
            M_incX = taxitita
        else:
            M_incX = - taxitita
        if FoudasY > MitY:
            M_incY = taxitita
        else:
            M_incY = - taxitita
        MitX += M_incX
        MitY += M_incY
    #chaseeeeee 2
    if (MatX != FoudasX or MatY != FoudasY):
        taxitita = 0.2
        if flagover == 1:
            taxitita=0

        if FoudasX > MatX:
            Mat_incX = taxitita
        else:
            Mat_incX = - taxitita
        if FoudasY > MatY:
            Mat_incY = taxitita
        else:
            Mat_incY = - taxitita
        MatX += Mat_incX
        MatY += Mat_incY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # kinhsh FOuda
        if event.type == pygame.KEYDOWN:
            taxitita = 0.4
            if flagover == 1:
                taxitita = 0
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                FoudasImg = pygame.image.load("Foudas_panw.png")
                incY = -taxitita
                if BullState == "ready":
                    flag= 1
                    B_rateX = 0
                    B_rateY = -0.7
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                FoudasImg = pygame.image.load("Foudas_katw.png")
                incY = taxitita
                flag=0
                if BullState == "ready":
                    B_rateX = 0
                    B_rateY = 0.7
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                FoudasImg = pygame.image.load("Foudas_aristera.png")
                incX = -taxitita
                flag=0
                if BullState == "ready":
                    B_rateX = -0.7
                    B_rateY = 0
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                FoudasImg = pygame.image.load("Foudas.png")
                incX = taxitita

                flag =0
                if BullState == "ready":
                    B_rateX = 0.7
                    B_rateY = 0
            elif event.key == pygame.K_SPACE:
                if BullState == "ready":
                    sound = mixer.Sound("Heavy Sniper Sound Effect.wav")
                    sound.play()
                    BullX = FoudasX
                    BullY = FoudasY+25
                    if flag == 1:
                        BullX+=27

                    fire(BullX, BullY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                incY = 0.0
            elif event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                incX = 0.0

    FoudasX += incX
    FoudasY += incY
    if FoudasX <= 0:
        FoudasX = 0
    elif FoudasX >= 950:
        FoudasX = 950
    if FoudasY <= 0:
        FoudasY = 0
    elif FoudasY >= 550:
        FoudasY = 550
    if FoudasX > 110 and FoudasX < 150 and FoudasY < 223 and FoudasY > 125:
        FoudasX = 815
        FoudasY = 203
    elif FoudasX > 846 and FoudasX <888 and FoudasY > 126 and FoudasY< 203:
        FoudasX = 91
        FoudasY = 223
    if FoudasX > 307 and FoudasX < 348 and FoudasY > 47 and FoudasY < 110:
        FoudasX = 188
        FoudasY = 594
    elif FoudasX > 642 and FoudasX < 686 and FoudasY > 48 and FoudasY < 112:
        FoudasX = 825
        FoudasY = 517

    # bullet moving
    if (BullY > 600 or BullY<0) or (BullX>1000 or BullX<0):
        BullY = FoudasY
        BullState = "ready"
    if BullState == "fire":
        fire(BullX, BullY)
        BullY += B_rateY
        BullX += B_rateX

    #colision check
    colision = iscolision(MitX,MitY,BullX,BullY,35)
    if colision :
        BullState = "ready"
        kills += 1
        print(kills)
        MitX = random.randint(0, 1000)
        MitY = random.randint(0, 600)

    colision = iscolision(MatX, MatY, BullX, BullY,35)
    if colision:
        BullState = "ready"
        kills += 1
        MatX = random.randint(0, 1000)
        MatY = random.randint(0, 600)

#LIVES CHECK
    colision = iscolision(MitX, MitY, FoudasX, FoudasY,12)
    if colision:
        lives -= 1
        MitX = random.randint(0, 1000)
        MitY = random.randint(0, 600)


    colision = iscolision(MatX, MatY, FoudasX, FoudasY, 10)
    if colision:
        lives -= 1
        MatX = random.randint(0, 1000)
        MatY = random.randint(0, 600)
    Mit(MitX, MitY)
    Mat(MatX, MatY)
    Player(FoudasImg, FoudasX, FoudasY)

    pygame.display.update()

