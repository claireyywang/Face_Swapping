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

	visual_corresponding_point = False
	count = 0
	while (vidcap_s.isOpened() and vidcap_t.isOpened() and count < len_frame):
		[success_s, img_s] = vidcap_s.read()
		[success_t, img_t] = vidcap_t.read()

		if(not success_s or not success_t):
			break
		img_s_gray = cv2.cvtColor(img_s, cv2.COLOR_BGR2GRAY)
		img_t_gray = cv2.cvtColor(img_t, cv2.COLOR_BGR2GRAY)

		points_list_s = feature_detect(img_s_gray)
		points_list_t = feature_detect(img_t_gray)

		if(visual_corresponding_point):
			# Visualize the shape
			points_s = points_list_s[0]
			points_t = points_list_t[0]

			for j in range(26):
				(x, y) = points_s[j]
				cv2.circle(img_s, (x, y), 1, (255, 255, 0), -1)
			cv2.imshow("Output_1", img_s)
		
			for j in range(26):
				(x, y) = points_t[j]
				cv2.circle(img_t, (x, y), 1, (255, 255, 0), -1)
			cv2.imshow("Output_2", img_t)



		masks_s = extract_mask(points_list_s,img_s_gray)
		masks_t = extract_mask(points_list_t,img_t_gray)
		mask_t = masks_t[0]

		# From testing, take the first points_s in list as feature points 
		points_s = points_list_s[0]
		points_t = points_list_t[0]

		swap_img = warp_face(img_s_gray,img_t_gray,mask_t,points_s,points_t)
		count = count + 1





	cv2.destroyAllWindows()
	vidcap_s.release()
	vidcap_t.release()
