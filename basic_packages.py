'''
File clarification:
    import basic library such as numpy and so on
'''

import numpy as np
import matplotlib.pyplot as plt
import sys, os, math, scipy.misc, pdb, collections, random, imageio, cv2

from imutils import face_utils
from PIL import Image
from skimage.feature import corner_harris
from scipy.ndimage.filters import gaussian_filter
from numpy.linalg import inv

sys.path.append('../Convolutional_Neural_Networks/')

import PyNet as net
