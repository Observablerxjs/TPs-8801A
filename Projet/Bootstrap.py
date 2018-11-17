import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

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
        image = mpimg.imread('./asl_alphabet_test/A_test.jpg')
        edges = self.edgeDetec.detect_edges(image)
        plot = plt.imshow(edges)
        plt.show()

        clippedEdges = self.clip.clip(edges)
        plot = plt.imshow(clippedEdges)
        plt.show()
            

