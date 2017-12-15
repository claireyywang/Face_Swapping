'''
File clarification:
    import basic library such as numpy and so on
'''

import numpy as np
import matplotlib.pyplot as plt
import sys, os, math, scipy.misc, pdb, collections, random, imageio, cv2, dlib

from PIL import Image
from scipy.ndimage.filters import gaussian_filter
from scipy.spatial import ConvexHull
from matplotlib.path import Path
from numpy.linalg import inv

sys.path.append('../Convolutional_Neural_Networks/')

import PyNet as net



# Reference: https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
# face_utils functions
def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
 
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# return the list of (x, y)-coordinates
	return coords


def rect_to_bb(rect):
	# take a bounding predicted by dlib and convert it
	# to the format (x, y, w, h) as we would normally do
	# with OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	# return a tuple of (x, y, w, h)
	return (x, y, w, h)