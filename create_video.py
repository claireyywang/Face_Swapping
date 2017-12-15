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

		if(not success_s or not success_t):
			break
		img_s_gray = cv2.cvtColor(img_s, cv2.COLOR_BGR2GRAY)
		img_t_gray = cv2.cvtColor(img_t, cv2.COLOR_BGR2GRAY)

		points_list_s = feature_detect(img_s_gray)
		mask_s = extract_mask(points_list_s,img_s_gray)


		count = count + 1








	cv2.destroyAllWindows()
	vidcap.release()

