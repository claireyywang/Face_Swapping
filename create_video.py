from packages import *
from functions import * 

def create_video(file_path_s, file_path_t):
  s_video_queue = read_video(file_path_s)
  t_video_queue = read_video(file_path_t)

  img_s = np.array(s_video_queue[0])
  img_t = np.array(t_video_queue[0])

  h_s , w_s , l_s =  img_s.shape
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  #video_s = cv2.VideoWriter(output_path_s,fourcc,20,(w_s,h_s),True)

  h_t , w_t , l_t =  img_t.shape
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  #video_t = cv2.VideoWriter(output_path_t,fourcc,20,(w_t,h_t),True)

  s_features = feature_detect(img_s)
  t_features = feature_detect(img_t)
  
  #align_feature(s_landmarks[ALIGNMENT_REGIONS],t_landmarks2[ALIGNMENT_REGIONS])

if __name__ == '__main__':
  input_path_s = 'Input_Videos/Easy/FrankUnderwood.mp4'
  input_path_t = 'Input_Videos/Easy/MrRobot.mp4'

  len_frame = 200
  output_path_s = 'output_video/swap_s.avi' 
  output_path_t = 'output_video/swap_t.avi' 

  create_video(input_path_s,input_path_t)
