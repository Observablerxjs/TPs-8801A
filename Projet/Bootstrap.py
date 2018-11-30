import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np
import re
from PIL import Image

from Utils.ArgParser import ArgParser
from Classifier.DescriptorGenerator import DescriptorGenerator
from Pipeline.Pipeline import Pipeline

from Utils.ReadWrite import ReadWrite
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
            img = np.asarray(Image.open(p['input_image']).convert('L'))
            data = Pipeline().run(img)
            desc_i = DescriptorGenerator.generate_descriptor(data)

            descs = ReadWrite.read(p['model_path'])
            
            min_diff = float("inf")
            letter_actu = "_"

            for i in descs:
                nw_letter = i[0]
                nw_desc = [float(j) for j in re.findall(r"[\d.]+", i)]
                print(desc_i)
                print(nw_desc)
                dist_actu = DescriptorGenerator.distance(desc_i, nw_desc)
                if dist_actu < min_diff:
                    min_diff = dist_actu
                    letter_actu = nw_letter

            print(letter_actu)

        
        else:
            img = np.asarray(Image.open(p['input_image']).convert('L'))
            res = Pipeline().run(img)
            test = np.asarray(res[0])
            t = Image.fromarray(test)
            plot = plt.imshow(t)
            plt.show()
            print(res[1])

        
            

