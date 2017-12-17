from basic_packages import *
'''
	this is for image seamlessclone
	img_out_s with outbody_t
	img_out_t with outbody_s
'''

def face_blending(img_s, img_t, mask_s, mask_t, img_out_s, img_out_t):
    # center_s =np.array(ndimage.measurements.center_of_mass(mask_s))
    # center_t =np.array(ndimage.measurements.center_of_mass(mask_t))
    center_s =(img_s.shape[1]/2, img_s.shape[0]/2)
    center_t =(img_t.shape[1]/2, img_t.shape[0]/2)

    mask_s =mask_s*1
    mask_t =mask_t*1
    body_s =1 -mask_s
    body_t =1 -mask_t
    maskblend_s = img_s * body_s[..., np.newaxis] + img_out_t
    maskblend_t = img_t * body_t[..., np.newaxis] + img_out_s


    blend_s =cv2.seamlessClone(maskblend_s, img_s, mask_s, center_s, cv2.NORMAL_CLONE)
    blend_t =cv2.seamlessClone(maskblend_t, img_t, mask_t, center_t, cv2.NORMAL_CLONE)

    plt.figure()
    plt.imshow(np.uint8(maskblend_t))
    plt.figure()
    plt.imshow(np.uint8(maskblend_s))
    plt.show()
    return blend_s, blend_t