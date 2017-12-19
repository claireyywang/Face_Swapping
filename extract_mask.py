from packages import * 

# eyebrows, eyes, nose and mouth to create feature mask
OVERLAY_REGIONS = [list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42)), list(range(27, 35))+list(range(48, 61))]

def extract_mask(img, feature_points):
  #initialize mask based on source image size
  mask = np.zeros(img.shape[:2])
  for region in OVERLAY_REGIONS:
    mask_region = cv2.convexHull(feature_points[region])
    cv2.fillConvexPoly(mask, mask_region, color=1)
    
  mask = np.array([mask, mask, mask]).transpose((1, 2, 0))
  mask = (cv2.GaussianBlur(mask, (11, 11), 0) > 0) * 1.0
  mask = cv2.GaussianBlur(mask, (11, 11), 0)
  #import pdb; pdb.set_trace()
  #cv2.imwrite('mask.jpg', mask)
  return mask

if __name__ == '__main__':
  img_s = cv2.imread('report_pics/underwood1.jpg',cv2.IMREAD_COLOR)
  source_features = detect_feature(img_s)
  source_mask = extract_mask(img_s, source_features)
  plt.figure()
  plt.imshow(source_mask)
  plt.show()
