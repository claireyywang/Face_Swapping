from create_video import create_video

input_path_s = 'input_video/medium/LucianoRosso1.mp4'
input_path_t = 'input_video/medium/LucianoRosso2.mp4'

# input_path_s = 'input_video/easy/MrRobot.mp4'
# input_path_t = 'input_video/easy/Yuho.mp4'


len_frame = 200
output_path_s = 'output_video/swap_s.avi' 
output_path_t = 'output_video/swap_t.avi' 


create_video(input_path_s,input_path_t,len_frame,output_path_s,output_path_t)


