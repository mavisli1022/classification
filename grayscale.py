import numpy as np
import scipy
import os
from scipy.misc import imread
from scipy.misc import imresize
from scipy.spatial import distance
from scipy.misc import imsave
from os import listdir
from os.path import isfile, join
from PIL import Image



def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    grey = 0.2989*r + 0.5870*g + 0.1140*b
    return grey/255


def process_img(in_path, out_path):
    if not os.path.exists(in_path):
        return 'Input path does not exists, please enter a valid path'
    if os.path.exists(out_path):
        return 'Output path already exists, please enter a new path'
    else:
        os.makedirs(out_path)
        for f in listdir(in_path):
            if isfile(join(in_path, f)):
                image = rgb2gray(scipy.misc.imread(join(in_path, f)))
                imsave(join(out_path, f), image)