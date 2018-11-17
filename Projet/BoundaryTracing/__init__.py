import math

WHITE_PIXEL = 255


class BoundaryTracing:
    def __init__(self, image):
        self.image = image
        self.initial_trace_point = (0, 0)
        self.minx = self.calcul_minx()
        self.maxx = self.calcul_maxx()
        self.miny = self.calcul_miny()
        self.maxy = self.calcul_maxy()
        self.optimal_y = 0
        self.UD = 0
        self.LR = 0

    def run(self):
        self.optimal_y = self.optimal_y_level()
        self.initial_trace_direction()

    def optimal_y_level(self):
        dy = self.maxy - self.miny
        optimaly = math.floor(0.33 * dy)
        return optimaly

    def initial_trace_direction(self):
        self.initial_trace_point = (0, 0)
        for i in range(0, len(self.image[self.optimal_y])):
            if len(self.image[self.optimal_y][i]) == WHITE_PIXEL:
                self.initial_trace_point = (i, self.optimal_y)
                break
        x = self.initial_trace_point[0]
        y = self.initial_trace_point[1]
        self.UD = 1
        while y < self.miny and self.image[y][x] == WHITE_PIXEL:
            y = y - 1
        if y > 0 and x < len(self.image[y]):
            if self.image[y][x+1] == WHITE_PIXEL or self.image[y-1][x+1]:
                self.LR = -1
        if y > 0 and x > 0:
            if self.image[y][x-1] == WHITE_PIXEL or self.image[y-1][x-1]:
                self.LR = 1

    def trace(self):
        x = self.initial_trace_point[0]
        y = self.initial_trace_point[1]
        count = 0

    def calcul_minx(self):
        minx = 0
        for i in range(0, len(self.image[0])):
            for j in range(0, len(self.image)):
                if self.image[j][i] == WHITE_PIXEL:
                    minx = i
                    return minx
        return minx

    def calcul_maxx(self):
        maxx = 0
        for i in range(len(self.image[0]), 0, -1):
            for j in range(0, len(self.image)):
                if self.image[j][i] == WHITE_PIXEL:
                    maxx = i
                    return maxx
        return maxx


    def calcul_miny(self):
        miny = 0
        for i in range(0, len(self.image)):
            for j in range(0, len(self.image[i])):
                if self.image[i][j] == WHITE_PIXEL:
                    miny = i
                    return miny
        return miny

    def calcul_maxy(self):
        maxy = 0
        for i in range(len(self.image), 0, -1):
            for j in range(0, len(self.image[i])):
                if self.image[i][j] == WHITE_PIXEL:
                    maxy = i
                    return maxy
        return maxy

