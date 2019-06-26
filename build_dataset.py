from Configs import config
from imutils import paths
import shutil
import os

#loop over the data splits
for split in (config.TRAIN,config.TEST,config.VAL):
    print("[STATUS]processing '{} split'....".format(split))
    p = os.path.sep.join([config.ORIG_INPUT_DATASET,split])
    imagePaths = list(paths.list_images(p))

    #loop over the image paths.
    for imagePath in imagePaths:
        #extract class label from the file name.
        fileName = imagePath.split(os.path.sep)[-1]
        label = config.CLASSES[int(fileName.split("_")[0])]

        # construct the path to the output directory
        dirPath = os.path.sep.join([config.BASE_PATH,split,label])

        # if the output directory does not exist, create it
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        # construct the path to the output Image file and copy it.
        p = os.path.sep.join([dirPath,fileName])
        shutil.copy2(imagePath,p)
