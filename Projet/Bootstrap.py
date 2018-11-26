import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

from Utils.ArgParser import ArgParser
from Classifier.DescriptorGenerator import DescriptorGenerator
from Pipeline.Pipeline import Pipeline

from Training.Trainer import Trainer

from Shared.Borg import Borg
from Shared.Parameters import Parameters

class Bootstrap(Borg):
    def __init__(self):
        args = ArgParser.parse()
        Parameters.set_parameters({
            'mode' : args.mode,
            'input_image' : args.input_image,
            'training_set' : args.training_set,
            'model_path' :args.model_path
        })

    def run(self):
        p = Parameters().get_parameters()

        if p['mode'] == 'training': 
            Trainer().train()

        elif p['mode'] == 'classification':
            print('hello')
        
        else:
            img = np.asarray(Image.open('./asl_alphabet_test/I_test.jpg').convert('L'))
            res = Pipeline().run(img)
            test2 = np.asarray(res)
            test = Image.fromarray(test2)
            plot = plt.imshow(test)
            plt.show()

        
            

