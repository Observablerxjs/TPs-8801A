from PIL import Image
from os import listdir
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
        actu_letter = None
    
        training_data_files = listdir(self.path_data)
        print(training_data_files)

        centroid_actu_descriptor = DescriptorGenerator.generate_origin_descriptor()

        count = 0

        for i in range(0, len(training_data_files)):
            if training_data_files[i].split('_') == actu_letter:
                count = count + 1

                img = np.asarray(Image.open(self.path_data + training_data_files[i]).convert('L'))
                data = Pipeline().run(img)
                
                centroid_actu_descriptor = centroid_actu_descriptor + DescriptorGenerator.generate_descriptor(data)

            else:
                centroid_actu_descriptor = centroid_actu_descriptor / count
                ReadWrite.write(self.path_model, actu_letter + ' ' + centroid_actu_descriptor)

                actu_letter = training_data_files[i].split('_')
                centroid_actu_descriptor = DescriptorGenerator.generate_origin_descriptor()
                count = 0


