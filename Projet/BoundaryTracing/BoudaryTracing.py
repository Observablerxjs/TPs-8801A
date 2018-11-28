import math
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

WHITE_PIXEL = 255
BLACK_PIXEL = 0


class BoundaryTracing:
    def __init__(self):
        self.image = None
        self.minx = None
        self.maxx = None
        self.miny = None
        self.maxy = None
        self.initial_trace_point = (0, 0)
        self.UD = 0
        self.LR = 0

    def run(self, image):
        self.image = image.astype('uint8')
        self.minx = self.calcul_minx()
        self.maxx = self.calcul_maxx()
        self.miny = self.calcul_miny()
        self.maxy = self.calcul_maxy()
        self.initial_trace_direction()
        return self.trace()

    def flush(self):
        self.image = None
        self.minx = None
        self.maxx = None
        self.miny = None
        self.maxy = None

    # def optimal_y_level(self):
    #     print(self.maxy)
    #     print(self.miny)
    #     dy = self.maxy - self.miny
    #     optimaly = math.floor(0.33 * dy)
    #     return optimaly

    def initial_trace_direction(self):
        self.initial_trace_point = (0, 0)
        for i in range(self.minx, self.maxx):
            if self.image[self.maxy][i] != BLACK_PIXEL:
                self.initial_trace_point = (i, self.maxy)
                break
        x = self.initial_trace_point[0]
        y = self.initial_trace_point[1]
        self.UD = 1
        while y >= self.miny and self.image[y][x] != BLACK_PIXEL:
            y = y - 1
        if y > 0 and x < len(self.image[y]):
            if self.image[y][x+1] != BLACK_PIXEL or self.image[y-1][x+1]:
                self.LR = 1
        if y > 0 and x > 0:
            if self.image[y][x-1] != BLACK_PIXEL or self.image[y-1][x-1]:
                self.LR = -1

    def trace(self):
        x = self.initial_trace_point[0]
        y = self.initial_trace_point[1]
        count = 0

        ret_points = []
        fingertip = 0

        count_up = 0

        mask = np.zeros((len(self.image), len(self.image[0])))

        br = 0

        while x != self.maxx:

            br += 1

            if self.image[y][x] == BLACK_PIXEL:
                while self.image[y][x] == BLACK_PIXEL and x != self.maxx:
                    x += 1
                self.UD = 0
                self.LR = 1

            old_ud = self.UD

            if self.UD == 1:
                count_up += 1

            if (self.image[y][x-1] != BLACK_PIXEL and self.LR != 1) or\
                    (self.image[y][x + 1] != BLACK_PIXEL and self.LR != -1 and self.image[y+1][x+1] == BLACK_PIXEL):
                self.UD = 0
            elif (self.image[y - 1][x] != BLACK_PIXEL and self.UD != -1)or(self.image[y - 1][x - 1] != BLACK_PIXEL and self.LR == -1) or (self.image[y - 1][x + 1] != BLACK_PIXEL and self.LR == 1):
                self.UD = 1
            elif (self.image[y + 1][x] != BLACK_PIXEL and self.UD != 1) or (self.image[y + 1][x - 1] != BLACK_PIXEL and self.LR == -1) or (self.image[y + 1][x + 1] != BLACK_PIXEL and self.LR == 1):
                self.UD = -1

            if self.image[y - self.UD][x - 1] != BLACK_PIXEL and (self.LR != 1 or (old_ud == self.UD and self.UD != 0)):
                self.LR = -1
            elif self.image[y - self.UD][x + 1] != BLACK_PIXEL and (self.LR != -1 or (old_ud == self.UD and self.UD != 0)):
                self.LR = 1
            else:
                self.LR = 0

            if self.UD == 1:
                y = y - 1
            elif self.UD == -1:
                y = y + 1

            if self.LR == 1:
                x = x + 1
            elif self.LR == -1:
                x = x - 1

            count += 1
            if count == 5:
                mask[y][x] = 255
                count = 0

            ret_points.append([x, y])

            if count_up > 30 and self.UD == -1:
                fingertip += 1
                count_up = 0

            if self.UD != old_ud and self.UD == -1:
                count_up = 0

            if br == 1200:
                print('hello')
                break
        # test = np.asarray(self.image)
        # t = Image.fromarray(test)
        # plot = plt.imshow(t)
        # plt.show()
        return [mask, fingertip, ret_points]

    def calcul_minx(self):
        minx = 0
        for i in range(1, len(self.image[0]) - 1):
            for j in range(1, len(self.image) - 1):
                if self.image[j][i] != BLACK_PIXEL:
                    minx = i
                    return minx
        return minx

    def calcul_maxx(self):
        maxx = 0
        for i in range(len(self.image[0]) - 1, 0, -1):
            for j in range(1, len(self.image) - 1):
                if self.image[j][i] != BLACK_PIXEL:
                    maxx = i
                    return maxx
        return maxx

    def calcul_miny(self):
        miny = 0
        for i in range(1, len(self.image) - 1):
            for j in range(1, len(self.image[i]) - 1):
                if self.image[i][j] != BLACK_PIXEL:
                    miny = i
                    return miny
        return miny

    def calcul_maxy(self):
        maxy = 0
        for i in range(len(self.image) - 2, 0, -1):
            for j in range(1, len(self.image[i]) - 1):
                if self.image[i][j] != BLACK_PIXEL:
                    maxy = i
                    return maxy
        return maxy
