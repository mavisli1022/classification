import numpy as np
import scipy
import os
import csv
from scipy.misc import imread
from scipy.misc import imresize
from scipy.spatial import distance
import numpy as np
import scipy
import os
import csv
from scipy.misc import imread
from scipy.misc import imresize
from scipy.spatial import distance
from scipy.misc import imsave
from os import listdir
from os.path import isfile, join
from PIL import Image



def loadcsv():
    filename = 'train.csv'
    labels = np.zeros(7000)

    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        i = 0
        firstline = True
        for row in reader:
            if firstline:
                firstline = False
                continue
            else:
                labels[i] = int(row[1])
                i = i+1
    return labels


def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    grey = 0.2989*r + 0.5870*g + 0.1140*b
    return grey/255.


def saveToNpz():
    path = './train'
    subarray = []
    valid = []
    index = 0
    for f in listdir(path):
        if isfile(join(path, f)):
            index = index +1
            if (index <= 6500):
                subarray.append(rgb2gray(scipy.misc.imread(join(path, f))))
            if (index > 6500):
                valid.append(rgb2gray(scipy.misc.imread(join(path, f))))

    labels= loadcsv()
    labels_train = labels[:6500]
    labels_valid = labels[6500:]
    np.savez('./train.npz',inputs_train = subarray, target_train = labels_train, inputs_valid = valid, target_valid = labels_valid)



if __name__ == '__main__':
    saveToNpz()
