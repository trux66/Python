import pygame

# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 15
FRAMERATE = 35

# Define my classes
class Ball:
    RADIUS = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        global bgColor, fgColor
        newX = self.x = self.x + self.vx
        newY = self.y = self.y + self.vy

        if newX < BORDER + self.RADIUS:
            self.vx = - self.vx  # change direction is next to a border object
        elif newY < BORDER + self.RADIUS or newY > HEIGHT - BORDER - self.RADIUS:
            self.vy = - self.vy
        elif newX + self.RADIUS > WIDTH - Paddle.WIDTH and abs(newY - paddle.y) < Paddle.HEIGHT//2:
            self.vy = - self.vx
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColor)

class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(WIDTH - self.WIDTH, self.y - self.HEIGHT//2, WIDTH, HEIGHT))

    def update(self):
        global fgColor, bgColor
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fgColor)


# Draw the scenario
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgColor = pygame.Color("black")
fgColor = pygame.Color("white")

# fill the background
screen.fill(bgColor)

# Drawing the walls
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, WIDTH, HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))

# Create the ball and paddle
ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)
ball.show(fgColor)

paddle = Paddle(HEIGHT//2)
paddle.show(fgColor)

clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)
    # visualize the changes just made
    pygame.display.flip()
    paddle.update()
    ball.update()

pygame.quit()
