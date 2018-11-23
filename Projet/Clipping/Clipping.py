import numpy as np

WHITE_PIXEL = 255

class Clipping:
    def clip(self, edgesImage):
        self.image = edgesImage
        y1 = self.calculY1()
        y2 = self.calculY2()
        clipping_level = max(y1, y2)
        for i in range(clipping_level, len(self.image)):
            zeros = np.zeros(len(self.image[i]))
            self.image[i] = zeros
        return self.image

    def calculY1(self):
        y1 = len(self.image)
        for i in range(len(self.image) - 1, 0, -1):
            for j in range(0, len(self.image[i])):
                if j < len(self.image[i]) - 3:
                    if self.image[i][j] == WHITE_PIXEL and self.image[i][j+1] == WHITE_PIXEL and self.image[i][j+1] == WHITE_PIXEL:
                        y1 = i
                        return y1
        return y1

    def calculY2(self):
        y2 = len(self.image)
        diff = -1
        for i in range(len(self.image) - 1, 0, -1):
            first_white_pixel = -1
            last_white_pixel = len(self.image[i])
            for j in range(0,len(self.image[i])):
                if first_white_pixel != -1 and self.image[i][j] == WHITE_PIXEL:
                    first_white_pixel = j
                elif self.image[i][j] == WHITE_PIXEL:
                    last_white_pixel = j
            newdiff = last_white_pixel - first_white_pixel
            if diff == -1:
                diff = newdiff
            elif abs(diff - newdiff) > 10:
                y2 = i
                return y2
        return y2