from pygame import *
from random import randint
import math
import time
# initialize pygame
init()

# opening window
screen = display.set_mode((600 , 450))
display.set_caption("space invader")
# icon = image.load('')
# display.set_icon(icon)

# spaceship

spaceshipImg = image.load('./images/spaceship.png')
spaceshipX = 270
spaceshipY = 400
spaceshipX_change = 0

# background
backgroundImg = image.load('./images/bg1.jpg')

# invadar
invadarImg =[]
invadarX =[]
invadarY = []
invadarX_change = []
invadarY_change = []
no_of_enemies = 15

for i in range(no_of_enemies) :
    invadarImg.append(image.load('./images/invader.png'))
    invadarX.append(randint(0,540))
    invadarY.append(randint(0,200))
    invadarX_change.append(-1.2)
    invadarY_change.append(0)

# bullet
bulletImg = image.load('./images/bullets.png')
bulletX = 0
bulletY = spaceshipY
bulletY_change = 0
bulletX_change = 0

# score 
score =0
font_obj = font.Font('freesansbold.ttf',25)
textX = 10
textY = 10

# game over font
font_obj2 = font.Font('freesansbold.ttf',60)
font_obj3 = font.Font('freesansbold.ttf', 30)
game_overX = 100
game_overY = 200
final_scoreY = 280

def game_over(x,y1,y2):
    game_over_text = font_obj2.render("GAME OVER", True , (150,0,0))
    final_score_text = font_obj3.render("Your Total Score :" + str(score),True, (0,0,150))

    screen.blit(game_over_text, (x,y1))
    screen.blit(final_score_text, (x + 50,y2))


def show_score(x,y):
    score_text = font_obj.render("Score : " + str(score) , True , (100,220,100))
    screen.blit(score_text , (x,y))

# functions to put the graphics on the screen
def background():
    screen.blit(backgroundImg,(0,0))

def spaceship():
    screen.blit(spaceshipImg,(spaceshipX,spaceshipY))

def invadar(invadars_no):
    for i in range(invadars_no):
        screen.blit(invadarImg[i], (invadarX[i] , invadarY[i]))

# working functions
def fire_bullet(x,y):
    global bullet_state
    screen.blit(bulletImg, (x+16,y+10))

def invadar_movement():
    global invadarX,invadarY,invadarX_change,invadarY_change
    for i in range(no_of_enemies):
        if invadarX[i] < 4:
            invadarX_change[i] = 1.2
            invadarY_change[i] = 40
       
        elif invadarX[i] >=540:
            invadarY_change[i] = 40
            invadarX_change[i] = -1.2
        else:
            invadarY_change[i] = 0

        invadarX[i] += invadarX_change[i]
        invadarY[i] += invadarY_change[i]

def spaceship_movement():
    global spaceshipX, spaceshipX_change,bulletX
    if spaceshipX <= 0:
        if spaceshipX_change > 0:
            pass
        else:
            spaceshipX_change = 0

    elif spaceshipX >=540:
        if spaceshipX_change < 0:
            pass
        else:
            spaceshipX_change = 0

    spaceshipX +=spaceshipX_change

def doesCollide(bulX,bulY,invX,invY):
    distance = math.sqrt(math.pow((bulX-invX),2) + math.pow((bulY-invY),2))

    if distance <27 :
        return True
    else:
        return False
   
# Game loop
running = True
while running : 
    

#    Event loop , takes cares of all the events 
    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                 spaceshipX_change = -1.5
            elif e.key == K_RIGHT:
                spaceshipX_change = 1.5

            elif e.key == K_SPACE:          
                bulletY_change = -7

              
        if e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_RIGHT:
               spaceshipX_change = 0
               
        
    screen.fill((0,0,0))   
    background()
    invadar(no_of_enemies)
    spaceship()
    spaceship_movement()
    invadar_movement()
    show_score(textX, textY)
    
    # manage firing
    bulletY += bulletY_change
    fire_bullet(spaceshipX, bulletY)
    if bulletY <-24:
        bulletY = spaceshipY
        bulletY_change = 0

    # collision effect
    for i in range(no_of_enemies):
        if doesCollide(spaceshipX+16,bulletY+10,invadarX[i],invadarY[i]):
            invadarX[i] = randint(0,540)
            invadarY[i] = randint(0,200)
            bulletY_change = -500
            score += 1
    
    # Game over
    for i in range(no_of_enemies):
        if invadarY[i] >= 380:
            game_over(game_overX,game_overY,final_scoreY)
            for j in range(no_of_enemies):
                invadarX_change[j] = 0
                invadarY_change[j] = 0
            bulletY_change = 0
            spaceshipX_change = 0
            running = False


    display.update()


