import os
import glob
import cv2
from PIL import Image
import numpy as np

curpath = os.path.abspath(os.curdir)

input_path="./UnformatedData/"
output_path="/TrainingSet/"
os.chdir(input_path)
images=glob.glob("*.png")
for img_path in images:
    img = cv2.imread(img_path)
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(img, 10, 0, 10, 10, cv2.BORDER_CONSTANT,value=BLACK)
    constant = Image.fromarray(constant)
    w, h = constant.size
    constant = np.asarray(constant.crop((0, 0, w, h - 20)))

    out = [i + "_" for i in img_path.split('_')[1:-1]]
    out.append(img_path.split('_')[-1])
    result = Image.fromarray(constant.astype(np.uint8))
    result.save(curpath + output_path + "".join(out))