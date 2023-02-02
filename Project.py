from PgLib import *

WIDTH, HEIGHT = 1280, 720
GRAVITY = 450

score = 0
lost = False

playerPos = vector((WIDTH / 2) - 100, HEIGHT - 60)

ballPos = vector(WIDTH / 2, 50)
ballVel = vector(random(-150, 150), 1)

# Called once at the start
def setup():
    createWindow(WIDTH, HEIGHT, False)
    title("Example Bouncy Ball Game")

def updatePlayer():
    global playerPos
    if keyDown("A") and playerPos.x > 0:
        playerPos.set(playerPos.x - 500 * deltaTime(), playerPos.y)
    elif keyDown("D") and playerPos.x < WIDTH - 200:
        playerPos.set(playerPos.x + 500 * deltaTime(), playerPos.y)

def updateBall():
    global ballPos, ballVel, score, lost

    ballVel.set(ballVel.x, ballVel.y + GRAVITY * deltaTime())
    ballPos.set(ballPos.x + ballVel.x * deltaTime(), ballPos.y + ballVel.y * deltaTime())

    if ballPos.x >= WIDTH:
        ballPos.set(WIDTH, ballPos.y)
        ballVel.set(-ballVel.x, ballVel.y)
    elif ballPos.x <= 0:
        ballPos.set(0, ballPos.y)
        ballVel.set(-ballVel.x, ballVel.y)

    if ballPos.x >= playerPos.x and ballPos.x <= playerPos.x + 200 and ballPos.y >= playerPos.y and ballPos.y <= playerPos.y + 30:
        ballPos.set(ballPos.x, playerPos.y)
        ballVel.set(ballVel.x + random(-125, 125), -ballVel.y)
        score += 1

    if ballPos.y >= HEIGHT:
        ballVel.set(0, 0)
        lost = True
        


# Called every frame
def update():
    background(0, 0, 0)

    updatePlayer()
    updateBall()

    circle(ballPos, 20, colour(0, 0, 255))
    

    rect(playerPos, 200, 30, colour(255, 255, 255))

    text(vector(WIDTH/2, 50), f"Score: {score}")
    if lost:
        text(vector(WIDTH/2, 100), "You Lose, ESC to exit")