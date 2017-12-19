from packages import *
from functions import * 

# eyebrows, eyes, nose, mouth, jaw and face to create affine transformation matrix
ALIGNMENT_REGIONS = list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42))+list(range(27, 35))+list(range(48, 61))

# eyebrows, eyes, nose and mouth to create feature mask
OVERLAY_REGIONS = [list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42)), list(range(27, 35))+list(range(48, 61))]

def create_video(file_path_s, file_path_t, len_frame,output_path_s, output_path_t):
  s_video_queue = read_video(file_path_s)
  t_video_queue = read_video(file_path_t)

  img_s = np.array(s_video_queue[0])
  img_t = np.array(t_video_queue[0])
  count = 0

  h_s , w_s , l_s =  img_s.shape
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  video_s = cv2.VideoWriter(output_path_s,fourcc,20,(w_s,h_s),True)

  h_t , w_t , l_t =  img_t.shape
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  video_t = cv2.VideoWriter(output_path_t,fourcc,20,(w_t,h_t),True)


  while count <= len_frame:
    img_s = np.array(s_video_queue[count])
    img_t = np.array(t_video_queue[count])

    s_features = detect_feature(img_s)
    t_features = detect_feature(img_t)
    source_pts = s_features[ALIGNMENT_REGIONS]
    target_pts = t_features[ALIGNMENT_REGIONS]
    M1 = est_affine_transform(source_pts, target_pts)
    M2 = est_affine_transform(target_pts, source_pts)

    source_binary_mask = extract_mask(img_s, s_features)
    target_binary_mask = extract_mask(img_t, t_features)

    warped_source_mask = warp_img(source_binary_mask, M1, img_t.shape)
    warped_target_mask = warp_img(target_binary_mask, M2, img_s.shape)
    warped_source_img = warp_img(img_s, M1, img_t.shape)
    warped_target_img = warp_img(img_t, M2, img_s.shape)

    combined_mask1 = np.max([target_binary_mask, warped_source_mask], axis=0)
    combined_mask2 = np.max([source_binary_mask, warped_target_mask], axis=0)
    blended_img1 = blend_img(img_t, warped_source_img, s_features)
    blended_img2 = blend_img(img_s, warped_target_img, t_features)
    
    output1 = img_t * (1.0 - combined_mask1) + blended_img1 * combined_mask1
    output2 = img_s * (1.0 - combined_mask2) + blended_img2 * combined_mask2
    video_t.write(np.uint8(output1))
    video_s.write(np.uint8(output2))
    print count 
    count += 1

  cv2.destroyAllWindows()
  video_t.release()
  video_s.release()
  print('finish swapping')

if __name__ == '__main__':
  input_path_t = 'Input_Videos/Easy/JonSnow.mp4'
  input_path_s = 'Input_Videos/Easy/MrRobot.mp4'

  len_frame = 200
  output_path_s = 'Output_Videos/test3.avi'
  output_path_t = 'Output_Videos/test4.avi'

  create_video(input_path_s,input_path_t, len_frame, output_path_s, output_path_t)
