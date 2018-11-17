import numpy as np
import math

from scipy.ndimage import gaussian_filter
from scipy.ndimage import sobel

class EdgeDetection:
    def __init__(self):
        self.threshold_1 = 220
        self.threshold_2 = 150

    def calc_offset(self, angle):
        dl = math.cos(angle) / abs(math.cos(angle))
        dk = math.sin(angle) / abs(math.sin(angle))
        return [dl, dk]
    
    def round_angles(self, angles):
        ret_angles = np.zeros(len(angles), len(angles[0]))
        comp = math.pi / 16

        for i in range(0, len(angles)):
            for j in range (0, len(angles[0])):
                for k in range(0, 7):
                    ret_angles[i][j] = k * math.pi / 8 if angles[i][j] - k * math.pi / 8 <= comp else ret_angles[i][j]

        return ret_angles
    
    def operator(self, operande):
        filtered_image = gaussian_filter(operande, 2)

        sobel_x = sobel(filtered_image, 0)
        sobel_y = sobel(filtered_image, 1)

        grad_mags = np.sqrt(np.square(np.matrix(sobel_x)) + np.square(np.matrix(sobel_y)))

        second_sobel_x = sobel(np.tolist(grad_mags), 0)
        second_sobel_y = sobel(np.tolist(grad_mags), 0)
        grad_angles = self.round_angles(np.atan(np.divide(np.matrix(second_sobel_y), np.matrix(second_sobel_x))))
        
        return [grad_mags, grad_angles]

    def non_maxima_supp(self, grad_image):
        grad_mags = np.tolist(grad_image[0])
        grad_angles = np.tolist(grad_image[1])

        for i in range(0, len(grad_mags)):
            for j in range(0, len(grad_mags[i])):
                if grad_mags[i][j] > 0:
                    l = i
                    k = j
                    offset = self.calc_offset(grad_angles[i][j])

                    dl = offset[0]
                    dk = offset[1]

                    while grad_mags[l][k] < grad_mags[l + dl][k + dk] or grad_mags[l][k] < grad_mags[l - dl][k - dk]:
                        
                        grad_mags[l][k] = 0

                        if grad_mags[l + dl][k + dk] > grad_mags[l - dl][k - dk]:
                            l = l + dl
                            k = k + dl
                        else:
                            l = l - dl
                            k = k - dk

                        offset = self.calc_offset(grad_angles[l][k])
                        dl = offset[0]
                        dk = offset[1]

    #calculate the mask in function of the tresholds.
    #2 indicates a strong edge. 1 indicates a weak edge. 0 indicates a edge to cut
    def class_thresholding(self, image_maxima):
        mask = np.tolist(np.zeros(len(image_maxima), len(image_maxima[0])))

        for i in range(0, len(image_maxima)):
            for j in range(0, len(image_maxima[i])):
                if (image_maxima[i][j] > self.threshold_1):
                    mask[i][j] = 2
                elif image_maxima[i][j] < self.threshold_1 and image_maxima[i][j] > self.threshold_2:
                    mask[i][j] = 1

    def hysterisis_rec(self, mask, l, k):
        no_more_edge = True
        
        for m in range(-1, 1):
            for n in range(-1, 1):
                if not(m == 0 and n == 0):
                    no_more_edge = True if mask[l + m][k + n] != 0 else no_more_edge

        if no_more_edge:
            return False

        res = False
        for m in range(-1, 1):
            for n in range(-1, 1):
                if not(m == 0 and n == 0) and mask[l + m][k + n] != 0:
                    res = res or self.hysterisis_rec(mask, l + m, k + n)

        res = res or mask[l, k] == 2

        return res

    def hysterisis(self, mask, maxima):
        for i in range(0, len(maxima)):
            for j in range(0, len(maxima[i])):
                if mask[i][j] == 1:
                    is_strong = self.hysterisis_rec(mask, i, j)
                    if is_strong:
                        mask[i][j] = 2
                    else:
                        mask[i][j] = 0



    def apply_mask(self, mask, maxima):
        mask = np.tolist(np.matrix(mask) / 2)
        return np.tolist(np.matrix(mask) * np.matrix(maxima)) 


    def detect_edges(self, image):
        grad_image = self.operator(image)
        
        image_maxima = self.non_maxima_supp(grad_image)
        
        maxima_and_mask = self.class_thresholding(image_maxima)
        maxima_and_updated_mask = self.hysterisis(maxima_and_mask[0], maxima_and_mask[1])

        return self.apply_mask(maxima_and_updated_mask[0], maxima_and_updated_mask[1])






