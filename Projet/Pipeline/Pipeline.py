from EdgeDetection.EdgeDetection import EdgeDetection
from Clipping.Clipping import Clipping
from BoundaryTracing.BoudaryTracing import BoundaryTracing

from Shared.Borg import Borg

class Pipeline(Borg):
    def __init__(self):
        self.edgeDetec = EdgeDetection()
        self.clip = Clipping()
        self.boundTrac = BoundaryTracing()

    def run(self, input):
        edges_image = self.edgeDetec.detect_edges(input)
        clipped_image = self.clip.clip(edges_image)
        self.boundTrac.run(clipped_image)
        return clipped_image
