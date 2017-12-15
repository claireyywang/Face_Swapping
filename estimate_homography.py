'''
input: 
	points_s: list of points
	points_t: list of points
	idx_s: int, the ith points in points_s list
	idx_t: int, the ith points in points_t list

output:
	H: the homography transformation transform from idx_s to idx_t
'''

from basic_packages import *

def estimate_homography(points_list_s,points_list_t,idx_s,idx_t):
	points_s = points_list_s[idx_s]
	points_t = points_list_t[idx_t]
	H = est_homography(points_s[0:26,0],points_s[0:26,1], points_t[0:26,0], points_t[0:26,1])
	return H