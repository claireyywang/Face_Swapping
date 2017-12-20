from packages import *


def detect_feature(img):
  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor('dlib/shape_predictor_68_face_landmarks.dat')
  rects = detector(img, 1)
  #all_features_points = []
  for rect in rects:
    # 68*2 element matrix represent feature points 
    feature_points = np.matrix([[p.x, p.y] for p in predictor(img, rect).parts()])
    #all_features_points.append(feature_points)
  #all_features_points = np.matrix(all_features_points)
  return feature_points

if __name__ == '__main__':
  img_s = cv2.imread('report_pics/jonsnow1.jpg',cv2.IMREAD_COLOR)
  img_gray = cv2.cvtColor(img_s, cv2.COLOR_RGB2GRAY)
  source_features = detect_feature(img_s)
  plt.figure()
  plt.imshow(img_s)
  for feature in source_features:
    plt.plot(feature[0], feature[0], 'w+')
  plt.axis('off')
  plt.show()