import pygame

# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1

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
        self.show(bgColor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(fgColor)

class Paddle:
    pass

# Create objects
ballplay = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, 0)


# Draw the scenario
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bgColor = pygame.Color("black")
fgColor = pygame.Color("white")

pygame.draw.rect(screen, fgColor, pygame.Rect((0,0), (WIDTH,HEIGHT)))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))
screen.fill(bgColor)

ballplay.show(fgColor)

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    pygame.display.flip()
    ballplay.update()

pygame.quit()
