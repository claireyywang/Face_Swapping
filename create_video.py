from basic_packages import * 
from functions import *
'''
input: 
	file_path_s: the path of the mp4 file of source
	file_path_t: the path of the mp4 file of target
	len_frame: int
	file_output_path: the path of output video
'''

def create_video(file_path_s, file_path_t ,len_frame,file_output_path):

	vidcap_s = cv2.VideoCapture(file_path_s)
	vidcap_t = cv2.VideoCapture(file_path_t)

	count = 0
	while (vidcap_s.isOpened() and vidcap_t.isOpened() and count < len_frame):
		[success_s, img_s] = vidcap_s.read()
		[success_t, img_t] = vidcap_t.read()

		img_s = img_s[:, :, ::-1]
		img_t = img_t[:, :, ::-1]

		if(not success_s or not success_t):
			break
		img_s_gray = cv2.cvtColor(img_s, cv2.COLOR_RGB2GRAY)
		img_t_gray = cv2.cvtColor(img_t, cv2.COLOR_RGB2GRAY)

		'''
			detect all features points
		'''
		points_list_s = feature_detect(img_s_gray)
		points_list_t = feature_detect(img_t_gray)
		points_s =points_list_s[0].astype(np.float)
		points_t =points_list_t[0].astype(np.float)

		'''
			this is used to extract the face and obtain the binary mask
		'''
		masks_s = extract_mask(points_list_s,img_s_gray)
		mask_s = masks_s[0]
		masks_t = extract_mask(points_list_t,img_t_gray)
		mask_t = masks_t[0]

		'''
			apply face warping 1. from source to target 2. from target to source
		'''
		img_out_s, img_out_t = face_warping(points_s, points_t, img_s, img_t, mask_s, mask_t)

		'''
			this is for image seamlessclone
			img_out_s with outbody_t
			img_out_t with outbody_s
		'''
		blend_s, blend_t = face_blending(img_s, img_t, mask_s, mask_t, img_out_s, img_out_t)



		plt.figure()
		plt.imshow(img_out_s)
		plt.figure()
		plt.imshow(img_out_t)
		plt.show()





		# points_s is [y,x] instead of [x,y]
		# H = estimate_homography(points_list_s,points_list_t,0,0)
		# swap_img = warp_face(img_s_gray,img_t_gray,mask_t,H)
		count = count + 1





	cv2.destroyAllWindows()
	vidcap_s.release()
	vidcap_t.release()

if __name__=='__main__':
	input_path_s = '.\input_video\Yuho.mp4'
	input_path_t = '.\input_video\easy\FrankUnderwood.mp4'
	len_frame = 10
	output_path = '.\output_video\output.mp4'

	create_video(input_path_s, input_path_t, 10, output_path)