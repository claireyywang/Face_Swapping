'''
input: 
	img_s: source img H*W
	img_t: target img H*W
	mask_t: boolean matrix represent the mask of 
	H: the homography transformation matrix

output:
	img_out: the face finish warping

reference: 
	https://www.learnopencv.com/face-swap-using-opencv-c-python/
'''

from estimate_homography import estimate_homography
from basic_packages import *

def warp_face(img_s,img_t,mask_t,points_s,points_t):
	h_s,w_s = img_s.shape
	h_t,w_t = img_t.shape
	
	idxes_t = np.asarray(np.where(mask_t == True))
	idxes_t_full = np.asarray([idxes_t[0],idxes_t[1],np.ones(idxes_t[0].size)])	

	# H is the homography from T points to S points
	H_s = estimate_homography(points_s,points_t,idxes_t[0,:],idxes_t[1,:],img_s,img_t)

	idxes_s = np.zeros(idxes_t.shape)
	count = 0
	for H in H_s:
		idxes_s[:,count] = (np.dot(H,idxes_t_full[:,count]))
		count = count + 1
		# idxes_s = (np.around(idxes_s_full[0:2]))

	# take pixel value from source img
	img_t_copy = np.copy(img_t)
	x_s = idxes_s[0,:].astype(int)
	y_s = idxes_s[1,:].astype(int)
	x_t = idxes_t[0,:].astype(int)
	y_t = idxes_t[1,:].astype(int)
	x_s[x_s >= h_s] = h_s-1
	y_s[y_s >= w_s] = w_s-1

	pdb.set_trace()
	img_t_copy[x_t,y_t] = img_s[x_s,y_s]
	plt.imshow(img_t_copy)
	plt.show()

	return 0
