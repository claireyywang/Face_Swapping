from packages import *
from align_feature import * 

def est_affine_transform(source_pts, target_pts):
  source_pts = source_pts.astype(np.float64)
  target_pts = target_pts.astype(np.float64)

  #calculate centroid form for each feature points set
  s_mean = np.mean(source_pts, axis=0)
  t_mean = np.mean(target_pts, axis=0)

  #adjust feature points by centroid form
  #translation
  source_pts -= s_mean
  target_pts -= t_mean

  #adjust by standard deviation for scaling
  #uniform scaling
  s_std = np.std(source_pts)
  t_std = np.std(target_pts)
  source_pts /= s_std
  target_pts /= t_std

  #calculate rotation matrix
  #Rotation
  U, S, VT = np.linalg.svd(source_pts.T * target_pts)
  R = (U * VT).T
  
  M1 = (t_std/s_std)*R
  M2 = t_mean.T-(t_std/s_std)*R*s_mean.T
  M3 = np.matrix([0., 0., 1.])

  # compute affine transformation matrix
  M = np.vstack([np.hstack((M1,M2)),M3])
  return M

if __name__ == '__main__':
  img_s = cv2.imread('report_pics/underwood1.jpg',cv2.IMREAD_COLOR)
  img_t = cv2.imread('report_pics/mr_robot1.jpg',cv2.IMREAD_COLOR)
  img_gray_s = cv2.cvtColor(img_s, cv2.COLOR_RGB2GRAY)
  img_gray_t = cv2.cvtColor(img_t, cv2.COLOR_RGB2GRAY)
  source_features= detect_feature(img_gray_s)
  target_features = detect_feature(img_gray_t)

  source_pts = source_features[ALIGNMENT_REGIONS]
  target_pts = target_features[ALIGNMENT_REGIONS]
  M = est_affine_transform(source_pts, target_pts)
  print M