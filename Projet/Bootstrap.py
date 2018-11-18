import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

from EdgeDetection.EdgeDetection import EdgeDetection
from Clipping.Clipping import Clipping

class Bootstrap:
    def __init__(self):
        #self.iimProc =
        #self.fingDetec =
        self.edgeDetec = EdgeDetection()
        self.clip = Clipping()
        #self.classifier = 
        #self.boundTrac =

    def run(self):
        #if

        #else:
            #processedImage = 
        img = Image.open('./asl_alphabet_test/C_test.jpg').convert('L')
        image = np.asarray(img)

        edges = self.edgeDetec.detect_edges(image)

        test2 = np.asarray(edges)
        test = Image.fromarray(test2)
        plot = plt.imshow(test)
        plt.show()

        #clippedEdges = self.clip.clip(edges)
        #plot = plt.imshow(clippedEdges)
        #plt.show()
            

