import os, time

class Canvas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.canvas = [["\033[0;0;0m " for y in range(self.y)] for x in range(self.x)]
    def drawCanvas(self):
        os.system("clear")
        for y in range(self.y):
            if y > 0:
                print("\033[0;0;0m ")
            for x in range(self.x):
                print(self.canvas[x][y], end="")
        print("\033[0;0;0m ")
    def putPoint(self, x, y, character):
        self.canvas[x][y] = character
    def clearPoint(self, x, y):
        self.canvas[x][y] = "\033[0;0;0m "
    def update(self, tileArray):
        for i, tile in enumerate(tileArray):
            self.putPoint(abs(tile[0]), abs(tile[1]), tile[2])
    def clearCanvas(self):
        self.canvas = [["\033[0;0;0m " for y in range(self.y)] for x in range(self.x)]
    def putLine(self, x1, y1, x2, y2, character):
        dx = x2-x1
        dy = y2-y1
        if dx == 0:
            for y in range(y1, y2+1):
                self.canvas[x2][y] = character
        else:
            for x in range(x1, x2):
                y = int(round(y1+dy*(x-x1)/dx))
                self.canvas[x][y] = character
