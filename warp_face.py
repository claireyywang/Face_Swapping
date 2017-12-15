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

from basic_packages import *

def warp_face(img_s,img_t,mask_t,H):
	h_s,w_s = img_s.shape
	h_t,w_t = img_t.shape

	invH = inv(H)
	
	# inv(H) * target_point = source_point
	idxes_t = np.asarray(np.where(mask_t == True))
	idxes_t_full = np.asarray([idxes_t[0],idxes_t[1],np.ones(idxes_t[0].size)])	
	idxes_s_full = np.dot(H,idxes_t_full)
	idxes_s_full = np.divide(idxes_s_full,idxes_s_full[2])
	idxes_s = (np.around(idxes_s_full[0:2])).astype(int)

	# take pixel value from source img
	img_t_copy = np.copy(img_t)
	x_s = idxes_s[0,:]
	y_s = idxes_s[1,:]
	x_t = idxes_t[0,:]
	y_t = idxes_t[1,:]
	x_s[x_s >= h_s] = h_s-1
	y_s[y_s >= w_s] = w_s-1

	pdb.set_trace()
	img_t_copy[x_t,y_t] = img_s[x_s,y_s]
	plt.imshow(img_t_copy)
	plt.show()
	return 0
