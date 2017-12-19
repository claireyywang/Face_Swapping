from packages import *

def read_video(video_path):
  cap = cv2.VideoCapture(video_path)
  count = 0
  img_queue = []
  success = 1
  while success: 
  	success,image = cap.read()
  	if not success:
  		print "failed to read in video"
  	print('Read a new frame: ', success)
  	img_queue.append(image)
  	count += 1
  cap.release()
  return img_queue

if __name__ == '__main__':
  video_path = 'Input_Videos/Easy/MrRobot.mp4'
  img_queue = read_video(video_path)
  cv2.imwrite('mr_robot.jpg', img_queue[0])
  print len(img_queue)