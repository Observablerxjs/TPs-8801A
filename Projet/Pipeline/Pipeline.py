from EdgeDetection.EdgeDetection import EdgeDetection
from Clipping.Clipping import Clipping
from BoundaryTracing.BoudaryTracing import BoundaryTracing

from Shared.Borg import Borg

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

import numpy as np
from PIL import Image

class Pipeline(Borg):
    def __init__(self):
        self.edgeDetec = EdgeDetection()
        self.clip = Clipping()
        self.boundTrac = BoundaryTracing()

    def run(self, input):
        edges_image = self.edgeDetec.detect_edges(input)
        clipped_image = self.clip.clip(edges_image)
        bound_image_data = self.boundTrac.run(clipped_image)
        test = np.asarray(clipped_image)
        t = Image.fromarray(test)
        plot = plt.imshow(t)
        plt.show()
        return bound_image_data
