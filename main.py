from gamelib import *

def bee_update():
    bee.draw()
    if keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
        bee.x -= 10
        if bee.x <= 0:
            bee.x += 10
    if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
        bee.x += 10
        if bee.x >= 1200 :
            bee.x -= 10
    if keys.Pressed[K_UP] or keys.Pressed[K_w]:
        bee.y -= 10
        if bee.y <= 0:
            bee.y += 10
    if keys.Pressed[K_DOWN] or keys.Pressed[K_s]:
        bee.y += 10
        if bee.y >= 800:
            bee.y -= 10

def flower(flower, pollen):
    flower_update()
    flower.move()
    pollen.draw()
    x = randint(50, 300)
    if flower.x < -100:
        flower.y = 550
        flower.x = game.width + x
        flower.speed += 1
    pollen.y -= 10
    if pollen.y < 0:
        pollen.x = flower.x
        pollen.y = flower.y
        pollen.visible = True
    if bee.collidedWith(pollen):
        bee.pollen += 1
        pollen_S.play()
        pollen.visible = False

def flower_update():
    if flower_B.collidedWith(flower_R):
        flower_R.x += 20
    if flower_R.collidedWith(flower_Y):
        flower_Y.x += 25
    if flower_Y.collidedWith(flower_B):
        flower_B.x += 30

def cloud_update():
    if Cloud_Lightning.collidedWith(Cloud_Acid_Rain):
        Cloud_Acid_Rain.x += 50
    
def pollen_all():
    pollen_B.draw()
    pollen_B2.draw()
    pollen_B3.draw()
    pollen_R.draw()
    pollen_R2.draw()
    pollen_R3.draw()
    pollen_Y.draw()
    pollen_Y2.draw()
    pollen_Y3.draw()

game = Game(1200, 800, "Be a Bee")
bk = Image("./images/Background.png", game)
bk_D = Image("./images/Background_dark.png", game)
bk.resizeTo(game.width, game.height)
bk_D.resizeTo(game.width, game.height)
game.setBackground(bk)

bee = Animation("./images/Bee.png", 4, game, 1000 / 2, 1500 / 3)
bee.moveTo(800, 400)
bee.resizeBy(-70)
bee.setSpeed(4, 45)

honeycomb = Image("./images/Honeycomb.png", game)
honeycomb.resizeBy(-55)
honeycomb.moveTo(440, 410)

game_logo = Image("./images/Game Logo.png", game)
game_logo.resizeBy(100)
game_logo.moveTo(600, 300)

YL = Image("./images/youlose.png", game)
YL.resizeBy(30)
YW = Image("./images/youwin.png", game)
YW.resizeBy(30)
gameover = Image("./images/gameover.png", game)
gameover.resizeBy(30)

#flower
flower_B = Image("./images/Flower_Blue.png", game)
flower_B.resizeBy(-50)
flower_B.setSpeed(3, 90)
flower_B.y = 550
flower_R = Image("./images/Flower_Red.png", game)
flower_R.resizeBy(-50)
flower_R.setSpeed(3, 90)
flower_R.y = 550
flower_Y = Image("./images/Flower_Yellow.png", game)
flower_Y.resizeBy(-50)
flower_Y.setSpeed(3, 90)
flower_Y.y = 550

#Pollen
pollen_B = Image("./images/Pollen_Blue.png", game)
pollen_B.resizeBy(-85)
pollen_B.visible = False
pollen_R = Image("./images/Pollen_Red.png", game)
pollen_R.resizeBy(-85)
pollen_R.visible = False
pollen_Y = Image("./images/Pollen_Yellow.png", game)
pollen_Y.resizeBy(-85)
pollen_Y.visible = False
pollen_B2 = Image("./images/Pollen_Blue2.png", game)
pollen_B2.resizeBy(-90)
pollen_B2.visible = False
pollen_R2 = Image("./images/Pollen_Red2.png", game)
pollen_R2.resizeBy(-90)
pollen_R2.visible = False
pollen_Y2 = Image("./images/Pollen_Yellow2.png", game)
pollen_Y2.resizeBy(-90)
pollen_Y2.visible = False
pollen_B3 = Image("./images/Pollen_Blue3.png", game)
pollen_B3.resizeBy(-91)
pollen_B3.visible = False
pollen_R3 = Image("./images/Pollen_Red3.png", game)
pollen_R3.resizeBy(-91)
pollen_R3.visible = False
pollen_Y3 = Image("./images/Pollen_Yellow3.png", game)
pollen_Y3.resizeBy(-91)
pollen_Y3.visible = False

#Cloud
Cloud_Lightning = Image("./images/Cloud_Lightning.png", game)
Cloud_Lightning.resizeBy(-75)
Cloud_Lightning.setSpeed(3, 90)
Cloud_Lightning.y = 50
Cloud_Acid_Rain = Image("./images/Cloud_Acid_Rain.png", game)
Cloud_Acid_Rain.resizeBy(-75)
Cloud_Acid_Rain.setSpeed(3, 90)
Cloud_Acid_Rain.y = 50
Acid_Rain = Image("./images/Acid_Rain.png", game)
Acid_Rain.resizeBy(-75)
Acid_Rain.visible = False
Lightning = Image("./images/Lightning.png", game)
Lightning.resizeBy(-75)
Lightning.visible = False

#Sounds
lightning_S = Sound("./Sounds/lightning.wav", 0)
acid_rain = Sound("./Sounds/acid_rain.wav", 1)
lose = Sound("./Sounds/lose.wav", 2)
win = Sound("./Sounds/win.wav", 3)
pollen_S = Sound("./Sounds/pollen.wav", 4)


c = (0, 0, 0)
f = Font(c,  48, black, "Comic Sans MS")

#Start Screen
game.level = -1
while not game.over:
  game.processInput()
  game.scrollBackground("left", 4)
  bee_update()

  honeycomb.draw()
  game_logo.draw()

  #Start Game
  if bee.x >= 1150:
      game.over = True
      honeycomb.visivle = False
      bee.moveTo(200, 400)
      game.level += 2

  game.drawText(" To start the game, use “D” to fly right ", 150, 150, f)
  game.update(30)

#Level 1
bee.pollen = 0
if game.level == 1:
    game.over = False
while not game.over :
    game.processInput()
    game.scrollBackground("left", 4)
    bee_update()
    flower(flower_B, pollen_B)

    flower(flower_Y, pollen_Y)

    flower(flower_R, pollen_R)

    if bee.pollen >= 10:
        game.level += 1
        game.over = True

    game.drawText(" Game Level: " + str(game.level) , 10, 10, f)
    game.drawText(" Pollen: " + str(bee.pollen) + "/10", 10, 50, f)
    game.update(30)

#Level 2
bee.pollen = 0
if game.level == 2:
    game.over = False
while not game.over:
    game.processInput()
    game.scrollBackground("left", 4)
    bee_update()
    flower_update()
    flower_B.move()
    flower_R.move()
    flower_Y.move()
    pollen_all()

    #Blue Pollen
    x = randint(50, 300)
    if flower_B.x < -100:
        flower_B.y = 550
        flower_B.x = game.width + x
        flower_B.speed += 1

    pollen_Blue = []
    for i in range(randint(0, 3)):
        pollen_Blue.append(pollen_B)
        pollen_Blue.append(pollen_B2)
        pollen_Blue.append(pollen_B3)

        pollen_Blue[i].y -= 10
        if pollen_Blue[i].y < 0:
            pollen_Blue[i].x = flower_B.x
            pollen_Blue[i].y = flower_B.y
            pollen_Blue[i].visible = True
        if bee.collidedWith(pollen_Blue[i]):
            if bee.collidedWith(pollen_B):
                bee.pollen += 1

            if bee.collidedWith(pollen_B2):
                bee.pollen += 2

            if bee.collidedWith(pollen_B3):
                bee.pollen += 5
            pollen_Blue[i].visible = False
            pollen_S.play()

    #Red Pollen
    x = randint(50, 300)
    if flower_R.x < -100:
        flower_R.y = 550
        flower_R.x = game.width + x
        flower_R.speed += 1

    pollen_Red = []
    for i in range(randint(0, 3)):
        pollen_Red.append(pollen_R)
        pollen_Red.append(pollen_R2)
        pollen_Red.append(pollen_R3)

        pollen_Red[i].y -= 10
        if pollen_Red[i].y < 0:
            pollen_Red[i].x = flower_R.x
            pollen_Red[i].y = flower_R.y
            pollen_Red[i].visible = True
        if bee.collidedWith(pollen_Red[i]):
            if bee.collidedWith(pollen_R):
                bee.pollen += 1

            if bee.collidedWith(pollen_R2):
                bee.pollen += 2

            if bee.collidedWith(pollen_R3):
                bee.pollen += 5
            pollen_Red[i].visible = False
            pollen_S.play()

    #Yellow Pollen
    x = randint(50, 300)
    if flower_Y.x < -100:
        flower_Y.y = 550
        flower_Y.x = game.width + x
        flower_Y.speed += 1

    pollen_Yellow = []
    for i in range(randint(0, 3)):
        pollen_Yellow.append(pollen_Y)
        pollen_Yellow.append(pollen_Y2)
        pollen_Yellow.append(pollen_Y3)

        pollen_Yellow[i].y -= 10
        if pollen_Yellow[i].y < 0:
            pollen_Yellow[i].x = flower_Y.x
            pollen_Yellow[i].y = flower_Y.y
            pollen_Yellow[i].visible = True
        if bee.collidedWith(pollen_Yellow[i]):
            if bee.collidedWith(pollen_Y):
                bee.pollen += 1

            if bee.collidedWith(pollen_Y2):
                bee.pollen += 2

            if bee.collidedWith(pollen_Y3):
                bee.pollen += 5
            pollen_Yellow[i].visible = False
            pollen_S.play()


    if bee.pollen >= 100:
        game.level += 1
        game.over = True

    game.drawText(" Game Level: " + str(game.level) , 10, 10, f)
    game.drawText(" Pollen: " + str(bee.pollen) + "/100", 10, 50, f)
    game.update(30)
    
#Level 3
bee.pollen = 0
game.setBackground(bk_D)
if game.level == 3:
    game.over = False

while not game.over:
    game.processInput()
    game.scrollBackground("left", 4)
    bee_update()
    flower_update()
    flower_B.move()
    flower_R.move()
    flower_Y.move()
    pollen_all()
    Cloud_Lightning.move()
    Cloud_Acid_Rain.move()
    Lightning.draw()
    Acid_Rain.draw()
    cloud_update()
    
    #Blue Pollen
    x = randint(50, 300)
    if flower_B.x < -100:
        flower_B.y = 550
        flower_B.x = game.width + x
        flower_B.speed += 1

    pollen_Blue = []
    for i in range(randint(0, 3)):
        pollen_Blue.append(pollen_B)
        pollen_Blue.append(pollen_B2)
        pollen_Blue.append(pollen_B3)

        pollen_Blue[i].y -= 10
        if pollen_Blue[i].y < 0:
            pollen_Blue[i].x = flower_B.x
            pollen_Blue[i].y = flower_B.y
            pollen_Blue[i].visible = True
        if bee.collidedWith(pollen_Blue[i]):
            if bee.collidedWith(pollen_B):
                bee.pollen += 1

            if bee.collidedWith(pollen_B2):
                bee.pollen += 2

            if bee.collidedWith(pollen_B3):
                bee.pollen += 5
            pollen_Blue[i].visible = False
            pollen_S.play()
            
    #Red Pollen
    x = randint(50, 300)
    if flower_R.x < -100:
        flower_R.y = 550
        flower_R.x = game.width + x
        flower_R.speed += 1

    pollen_Red = []
    for i in range(randint(0, 3)):
        pollen_Red.append(pollen_R)
        pollen_Red.append(pollen_R2)
        pollen_Red.append(pollen_R3)

        pollen_Red[i].y -= 10
        if pollen_Red[i].y < 0:
            pollen_Red[i].x = flower_R.x
            pollen_Red[i].y = flower_R.y
            pollen_Red[i].visible = True
        if bee.collidedWith(pollen_Red[i]):
            if bee.collidedWith(pollen_R):
                bee.pollen += 1

            if bee.collidedWith(pollen_R2):
                bee.pollen += 2

            if bee.collidedWith(pollen_R3):
                bee.pollen += 5
            pollen_Red[i].visible = False
            pollen_S.play()
            
    #Yellow Pollen
    x = randint(50, 300)
    if flower_Y.x < -100:
        flower_Y.y = 550
        flower_Y.x = game.width + x
        flower_Y.speed += 1

    pollen_Yellow = []
    for i in range(randint(0, 3)):
        pollen_Yellow.append(pollen_Y)
        pollen_Yellow.append(pollen_Y2)
        pollen_Yellow.append(pollen_Y3)

        pollen_Yellow[i].y -= 10
        if pollen_Yellow[i].y < 0:
            pollen_Yellow[i].x = flower_Y.x
            pollen_Yellow[i].y = flower_Y.y
            pollen_Yellow[i].visible = True
        if bee.collidedWith(pollen_Yellow[i]):
            if bee.collidedWith(pollen_Y):
                bee.pollen += 1

            if bee.collidedWith(pollen_Y2):
                bee.pollen += 2

            if bee.collidedWith(pollen_Y3):
                bee.pollen += 5
            pollen_Yellow[i].visible = False
            pollen_S.play()

    #Cloud
    x = randint(50, 100)
    y = randint(50, 100)
    if Cloud_Lightning.x < -100:
        Cloud_Lightning.y = y
        Cloud_Lightning.x = game.width + x
        Cloud_Lightning.speed += 1
    if Cloud_Acid_Rain.x < -100:
        Cloud_Acid_Rain.y = y
        Cloud_Acid_Rain.x = game.width + x
        Cloud_Acid_Rain.speed += 1

    Lightning_C = []
    Acid_Rain_C = []
    for i in range(randint(0, 5)):
        Lightning_C.append(Lightning)
        
        Lightning_C[i].y += 5
        if Lightning_C[i].y > 800:
            Lightning_C[i].x = Cloud_Lightning.x
            Lightning_C[i].y = Cloud_Lightning.y
            Lightning_C[i].visible = True
        if bee.collidedWith(Lightning_C[i]):
            bee.health -= 10
            lightning_S.play()
            Lightning_C[i].visible = False

    for i in range(randint(0, 5)):
        Acid_Rain_C.append(Acid_Rain)

        Acid_Rain_C[i].y += 5
        if Acid_Rain_C[i].y > 800:
            Acid_Rain_C[i].x = Cloud_Acid_Rain.x
            Acid_Rain_C[i].y = Cloud_Acid_Rain.y
            Acid_Rain_C[i].visible = True
        if bee.collidedWith(Acid_Rain_C[i]):
            bee.health -= 10
            acid_rain.play()
            Acid_Rain_C[i].visible = False

    if bee.health <= 0:
        game.over = True
        game.level += 2
        lose.play()
    if bee.pollen >= 100:
        game.level += 1
        game.over = True
        win.play()

    game.drawText(" Game Level: " + str(game.level) , 10, 10, f)
    game.drawText(" Pollen: " + str(bee.pollen) + "/100", 10, 50, f)
    game.drawText(" Health: " + str(bee.health) + "/100", 10, 90, f)
    game.update(30)

#Game Over
game.over = False
game.setBackground(bk)
while not game.over:
    game.processInput()
    game.scrollBackground("left", 4)
    gameover.draw()
    gameover.moveTo(600, 200)
    if game.level == 4:
        YW.draw()
        YW.moveTo(600, 350)
    if game.level == 5:
        YL.draw()
        YL.moveTo(600, 350)
    game.update(30)

game.quit()
