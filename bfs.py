import pygame
import time

WIDTH = 800
HEIGHT = 800

PADDING = 50

board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
]

# colors
GREY = (192, 192, 192)
BLACK = (0, 0, 0)
DEEP_BLUE = (128, 128, 128)
RED = (192, 32, 32)

# functions
def draw_board(screen):
    rows = len(board)
    lines = len(board[0])
    
    m = rows + 1
    n = lines + 1
    
    # grid height
    gh = (HEIGHT - PADDING * 2) // rows
    gw = (WIDTH - PADDING * 2) // lines

    for i in range(rows):
        for j in range(lines):
            if (board[i][j] == 1):
                pygame.draw.rect(screen, DEEP_BLUE, 
                    (PADDING + j * gw, PADDING + i * gh, gw, gh))
    
    for i in range(m):
        pygame.draw.line(screen, BLACK,
            (PADDING, PADDING + i * gh),
            (WIDTH - PADDING, PADDING + i * gh), 1)
            
    for i in range(n):
        pygame.draw.line(screen, BLACK,
            (PADDING + i * gw, PADDING),
            (PADDING + i * gw, HEIGHT - PADDING), 1)

queue = []
vd = []
prev = {}

def isValid(p, board, m, n):
    if board[p[1]][p[0]] == 1:
        return False
        
    if p[0] < 0 or p[1] < 0:
        return False
        
    if p[0] >= m or p[1] >= n:
        return False
       
    return True
    
def isEdge(p, m, n):
    if p[1] == 0 or p[0] == 0:
        return True
        
    if p[0] == m - 1 or p[1] == n - 1:
        return True
        
    return False
 
def visited(p):
    if p in vd:
        return True
    else:
        return False

def show_path(p):
    rows = len(board)
    lines = len(board[0])
    
    m = rows + 1
    n = lines + 1
    
    # grid height
    gh = (HEIGHT - PADDING * 2) // rows
    gw = (WIDTH - PADDING * 2) // lines
    
    while (p):
        pygame.draw.rect(screen, RED,
            (PADDING + gw * p[0], PADDING + gh * p[1], gw, gh))
        p = prev[p]
    
#
# m rows, n lines.
#
def solve(p, board, m, n): # p = (1, 3)
    queue.append(p)
    prev[p] = None
    vd.append(p)
    while (len(queue) > 0):
        p1 = queue.pop(0)
        
        steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for s in steps:
            p2 = (p1[0] + s[0], p1[1] + s[1])
            
            if (not isValid(p2, board, m, n)):
                continue
                
            if (visited(p2)):
                continue
        
            queue.append(p2)
            vd.append(p2)
            prev[p2] = p1
            
            if (not isEdge(p2, m, n)):
                continue
                
            show_path(p2)
            return

    print("can not find")            

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(GREY)
draw_board(screen)
solve((5, 5), board, 10, 10)
pygame.display.update()

going = True
while going:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            going = False
            
    time.sleep(0.016)
            
pygame.quit()