import os
import glob
import cv2

curpath = os.path.abspath(os.curdir)

input_path="./UnformatedData/"
output_path="/TrainingSet/"
os.chdir(input_path)
images=glob.glob("*.png")
Length=[]
Width=[]
for img_path in images:
    img = cv2.imread(img_path)
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT,value=BLACK)
    out = [i + "_" for i in img_path.split('_')[1:-2]]
    out.append(img_path.split('_')[-1])
    with open(curpath + output_path + "".join(out), 'wb+') as f:
        f.write(constant)