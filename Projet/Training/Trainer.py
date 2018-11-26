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

        actu_letter = training_data_files[0].split('_')[0]

        centroid_actu_descriptor = np.array(DescriptorGenerator.generate_origin_descriptor())

        count = 0

        for i in range(0, len(training_data_files)):
            if training_data_files[i].split('_')[0] == actu_letter:
                count = count + 1

                img = np.asarray(Image.open(self.path_data + training_data_files[i]).convert('L'))
                data = Pipeline().run(img)
                
                centroid_actu_descriptor = np.array(centroid_actu_descriptor) + np.array(DescriptorGenerator.generate_descriptor(data))

            else:
                centroid_actu_descriptor = centroid_actu_descriptor / count
                ReadWrite.write(self.path_model, actu_letter + ' '.join(centroid_actu_descriptor.tolist()))

                actu_letter = training_data_files[i].split('_')
                centroid_actu_descriptor = DescriptorGenerator.generate_origin_descriptor()
                count = 0


