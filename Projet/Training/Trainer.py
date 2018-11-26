from PIL import Image
from os import listdir, walk
import numpy as np

from Utils.ReadWrite import ReadWrite
from Classifier.DescriptorGenerator import DescriptorGenerator
from Pipeline.Pipeline import Pipeline

from Shared.Borg import Borg
from Shared.Parameters import Parameters

class Trainer(Borg):
    def __init__(self):
        p = Parameters.get_parameters()
        self.path_data = p['training_set']
        self.path_model = p['model_path']

    def train(self):
        training_data_files = listdir(self.path_data)

        descs = {}

        for i in range(0, len(training_data_files)):
            actu_letter = training_data_files[i].split('_')[0]

            if not(actu_letter in descs):
                descs[actu_letter] = [DescriptorGenerator.generate_origin_descriptor(), 0]

            img = np.asarray(Image.open(self.path_data + training_data_files[i]).convert('L'))
            data = Pipeline().run(img)
            nw_desc = DescriptorGenerator.generate_descriptor(data)

            descs[actu_letter] = np.array(descs[actu_letter]) + np.array([nw_desc, 1])

        for key in descs:
            data_to_add = np.array(descs[key][0]) / descs[key][1]
            ReadWrite.write(self.path_model, key + " ".join(str(x) for x in data_to_add.list()))


