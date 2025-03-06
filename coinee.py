import pgzrun
from random import randint
from pgzero.actor import Actor
WIDTH = 1500
HEIGHT = 750
score = 0
game_over = False
fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
back=Actor("back")
lose=Actor("lose")
win=Actor("win")
def draw():
    back.draw()
    fox.draw()
    coin.draw()
    screen.draw.text("Your Score : " + str(score), color="white", topleft=(10, 10))
    screen.draw.text("To Win A Choclate = Score **150**", color="white", topright=(1490,10))
    if (game_over and score<100):
        screen.fill("white")
        lose.draw()
        screen.draw.text("GAME OVER ! ", topleft=(540, 300), fontsize=100,color="black")
        screen.draw.text("You Scored " + str(score), topleft=(625, 375), fontsize=60,color="black")
    elif(game_over and score>=100):
        screen.fill("white")
        win.draw()
        screen.draw.text(" YOU WIN ! "+ str(score), topleft=(588,610), fontsize=65,color="black")
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
def time_up():
    global game_over
    game_over = True
def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 8
    elif keyboard.right:
        fox.x = fox.x + 8
    elif keyboard.up:
        fox.y = fox.y - 8
    elif keyboard.down:
        fox.y = fox.y + 8
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        score = score + 5
        place_coin()
clock.schedule(time_up,60.0)
place_coin()
pgzrun.go()

