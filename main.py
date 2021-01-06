import pygame
import math
# import Spot
from queue import PriorityQueue

WIDTH = 800
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* PATH FINDING")

# colors = {
#     "RED": ["255", "0", "0"],
#     "GREEN": ["0", "255", "0"],
#     "BLUE": ["0", "0", "255"],
#     "YELLOW": ["255", "255", "0"],
#     "WHITE": ["255", "255", "255"],
#     "BLACK": ["0", "0", "0"],
#     "PURPLE": ["128", "0", "128"],
#     "ORANGE": ["255", "165", "0"]
#     "GRAY": ["128", "128", "128"],
#     "TURQUOISE": ["64", "224", "208"]
# }


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def GetPosition(self):
        return self.row, self.col

    def GetClosed(self):
        return self.color == RED

    def GetOpen(self):
        return self.color == GREEN

    def GetBarrier(self):
        return self.color == BLACK

    def GetStart(self):
        return self.color == ORANGE

    def GetEnd(self):
        return self.color == TURQUOISE

    def Reset(self):
        return self.color == WHITE

    def SetClosed(self):
        self.color = RED

    def SetOpen(self):
        self.color = GREEN

    def SetBarrier(self):
        self.color = BLACK

    def SetStart(self):
        self.color = ORANGE

    def SetEnd(self):
        self.color = TURQUOISE

    def SetPath(self):
        self.color = PURPLE

    def Draw(self, WINDOW):
        pygame.draw.rect(
            WINDOW, self.color, (self.x, self.y, self.width, self.width))

    def UpdateNeighbors(self, grid):
        pass

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs((x1 - x2) + (y1 - y2))


def makeGrid(win, rows, width):
