import numpy as np

from scipy.interpolate import interp1d

class DescriptorGenerator:
    nb_points = 200
    desc_size = 20

    @staticmethod
    def generate_origin_descriptor():
        return [0] * (DescriptorGenerator.desc_size + 1)

    @staticmethod
    def generate_descriptor(data):
        nb_fingertips = data[1]
        array_index = data[2]

        xs = range(0, len(array_index))

        f = interp1d(xs, array_index)

        new_xs = np.linspace(0, len(xs), DescriptorGenerator.nb_points)
        new_ys = []

        for i in range(0, len(new_xs)):
            new_ys.append(f(new_xs[i]))

        new_ys = np.absolute(np.array(new_ys)).tolist()
        print(new_ys)
        new_ys = new_ys[-2]
        new_ys = (np.array(new_ys) / new_ys[0]).tolist()
        new_ys = new_ys[:DescriptorGenerator.desc_size]
        new_ys.append(nb_fingertips)

        return new_ys

    @staticmethod
    def distance(desc1, desc2):
        
