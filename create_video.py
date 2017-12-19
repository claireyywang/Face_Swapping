from packages import *
from functions import * 

# eyebrows, eyes, nose, mouth, jaw and face to create affine transformation matrix
ALIGNMENT_REGIONS = list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42))+list(range(27, 35))+list(range(48, 61))

# eyebrows, eyes, nose and mouth to create feature mask
OVERLAY_REGIONS = [list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42)), list(range(27, 35))+list(range(48, 61))]

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
  source_pts = s_features[ALIGNMENT_REGIONS]
  target_pts = t_features[ALIGNMENT_REGIONS]
  M = est_affine_transform(source_pts, target_pts)
  
  source_binary_mask = extract_mask(img_s, s_features)
  target_binary_mask = extract_mask(img_t, t_features)
  warped_mask = warp_img(source_binary_mask, M, img_t.shape)
  warped_source_img = warp_img(img_s, M, img_t.shape)
  
if __name__ == '__main__':
  input_path_s = 'Input_Videos/Easy/FrankUnderwood.mp4'
  input_path_t = 'Input_Videos/Easy/MrRobot.mp4'

  len_frame = 200
  output_path_s = 'output_video/swap_s.avi' 
  output_path_t = 'output_video/swap_t.avi' 

  create_video(input_path_s,input_path_t)
