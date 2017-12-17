from basic_packages import *

def face_extract(img):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('./dlib/shape_predictor_68_face_landmarks.dat')
    rects = detector(img, 1)
    points_list = []
    out_face =np.zeros_like(img)

    for (i, rect) in enumerate(rects):
        # Shape: the points of face feature
        shape = predictor(img, rect)
        points = shape_to_np(shape)
        points_list.append(points)

        remap_shape =np.zeros_like(points)
    feature_mask =np.zeros((img.shape[0], img.shape[1]))

    hull = ConvexHull(points_list[0])
    cv2.fillConvexPoly(img, hull, 1)
    feature_mask =feature_mask.astype(np.bool)
    out_face[feature_mask] =img[feature_mask]
    out_face.reshape(feature_mask.shape)

    cv2.imshow("mask_inv", out_face)