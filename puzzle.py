import time
import pygame

BLACK = (64, 64, 64)
WHITE = (192, 192, 192)
GRID_COLOR = (255, 255, 255)

NUM = 6

WIDTH = 800
HEIGHT = 600

HPADDING = 100
VPADDING = 20
GRID_WIDTH = (WIDTH - HPADDING * 2) // (NUM - 1)
GRID_HEIGHT = (HEIGHT - VPADDING * 2) // (NUM - 1)

EVT_MOVE = pygame.USEREVENT + 1


pygame.init()

board = [
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0]
]

visited = [[0 for i in range(NUM - 1)] for i in range(NUM - 1)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill((127, 127, 127))
# draw board
def draw_board():
    for y in range(NUM - 1): 
        line = board[y]
        for x in range(NUM - 1):
            e = line[x]
            if e == 0:
                pygame.draw.rect(screen, WHITE, 
                    ((HPADDING + x * GRID_WIDTH, VPADDING + y * GRID_HEIGHT), 
                        (GRID_WIDTH, GRID_HEIGHT)), 0)
            else:
                pygame.draw.rect(screen, BLACK, 
                    ((HPADDING + x * GRID_WIDTH, VPADDING + y * GRID_HEIGHT), 
                        (GRID_WIDTH, GRID_HEIGHT)), 0)

    for i in range(NUM):
        pygame.draw.line(screen, GRID_COLOR, (HPADDING, VPADDING + i * GRID_HEIGHT), 
            (WIDTH - HPADDING, VPADDING + i * GRID_HEIGHT))

    for i in range(NUM):
        pygame.draw.line(screen, GRID_COLOR, (HPADDING + i * GRID_WIDTH, VPADDING), 
            (HPADDING + i * GRID_WIDTH, HEIGHT - VPADDING))


draw_board()
pygame.display.update()

class Avatar(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        visited[y][x] = 1
        self.steps = [(x, y)]

    def move(self):
        if self.x == NUM - 2 and self.y == NUM - 2:
            return

        # try left
        tx = self.x - 1
        if tx >= 0 and board[self.y][tx] == 0 and visited[self.y][tx] != 1:
            self.x = tx
            visited[self.y][self.x] = 1
            self.steps.append((self.x, self.y))
            return

        # try down
        ty = self.y + 1
        if ty < NUM - 1 and board[ty][self.x] == 0 and visited[ty][self.x] != 1:
            self.y = ty
            visited[self.y][self.x] = 1
            self.steps.append((self.x, self.y))
            return

        # try right
        tx = self.x + 1
        if tx < NUM - 1 and board[self.y][tx] == 0 and visited[self.y][tx] != 1:
            self.x = tx
            visited[self.y][self.x] = 1
            self.steps.append((self.x, self.y))
            return

        # try up
        ty = self.y - 1
        if ty >= 0 and board[ty][self.x] == 0 and visited[ty][self.x] != 1:
            self.y = ty
            visited[self.y][self.x] = 1
            self.steps.append((self.x, self.y))
            return

        self.x, self.y = self.steps.pop()

    def draw(self):
        pygame.draw.circle(screen, (200, 50, 50), 
            (HPADDING + self.x * GRID_WIDTH + GRID_WIDTH // 2, VPADDING + self.y * GRID_HEIGHT + GRID_HEIGHT // 2), 
            GRID_HEIGHT // 2 - 10, 0)


avatar = Avatar(0, 0)

def move():
    screen.fill((127, 127, 127))
    avatar.move()
    draw_board()
    avatar.draw()
    pygame.display.update()

pygame.time.set_timer(EVT_MOVE, 1000)

going = True
while going:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            going = False

        elif evt.type == EVT_MOVE:
            move()

    time.sleep(0.04)
