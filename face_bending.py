from basic_packages import *
'''
	this is for image seamlessclone
	img_out_s with outbody_t
	img_out_t with outbody_s
'''

def face_blending(img_s, img_t, mask_s, mask_t, img_out_s, img_out_t):
    center_s =np.array(ndimage.measurements.center_of_mass(mask_s))
    center_t =np.array(ndimage.measurements.center_of_mass(mask_t))
    mask_s =mask_s*1
    mask_t =mask_t*1
    blend_s =cv2.seamlessClone(img_out_t, img_s, mask_s, round(center_s), cv2.NORMAL_CLONE)
    blend_t =cv2.seamlessClone(img_out_s, img_t, mask_t, round(center_t), cv2.NORMAL_CLONE)

    plt.figure()
    plt.imshow(img_out_s)
    plt.figure()
    plt.imshow(img_t)
    plt.show()
    return blend_s, blend_t