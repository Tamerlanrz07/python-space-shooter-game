# NOTE: This game uses images like "stand.png", "enemynewest.png", etc.
# Images are not included. Code demonstrates Python logic and structure only.
#pgzero





import random

WIDTH = 600
HEIGHT = 450

TITLE = "Space Journey"
FPS = 30
count = 0


# Objects and variables
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
type1 = Actor("ship1",(300,200))
type2 = Actor("ship2",(100,200))
type3 = Actor("ship3",(500,200))
mode = 'menu'
bullets = []


# Filling the enemy list
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)
    
# Filling the meteor list
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

# Drawing
def draw():
    # Game mode
    global count
    if mode == 'game':
        space.draw()
        planets[0].draw()
        for i in range(len(bullets)):
            bullets[i].draw()
        screen.draw.text(count,(10,10),color="white",fontsize=24)
        # Draw meteors
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        # Draw enemies
        for i in range(len(enemies)):
            enemies[i].draw()
    elif mode=="menu":
        space.draw()
        type1.draw()
        type2.draw()
        type3.draw()
        screen.draw.text("Choose your ship",center=(300,80),color="white",fontsize=29)
    # Game over screen
    elif mode == 'end':
        space.draw()
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text(count,(290 , 250), color = "white",fontsize=44)

# Controls
def on_mouse_move(pos):
    ship.pos = pos

# Add a new enemy to the list
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Enemy movement
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

# Planet movement
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

# Meteor movement
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

# Collisions
def collisions():
    global mode
    global count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for x in range(len(bullets)):
            if bullets[x].colliderect(enemies[i]):
                bullets.pop(x)
                enemies.pop(i)
                new_enemy()
                count = count + 1
                break

def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        for i in range(len(bullets)):
            if bullets[i].y <0 : 
                bullets.pop(i)
                break
            else : 
                bullets[i].y = bullets[i].y - 10

def on_mouse_down(button, pos):
    global mode
    global ship
    if mode=="menu" and type1.collidepoint(pos):
        ship.image="ship1"
        mode="game"
    elif mode=="menu" and type2.collidepoint(pos):
        ship.image="ship2"
        mode="game"
    elif mode=="menu" and type3.collidepoint(pos):
        ship.image="ship3"
        mode="game"
    
    elif button==mouse.LEFT and mode=="game":
        bullet=Actor("missiles")
        bullet.pos=ship.pos
        bullets.append(bullet)




