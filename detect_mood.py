from packages import *
from FeatureGen import *
from detect_feature import detect_feature

def detect_mood(img):
  emotions = {1: "Anger", 2: "Contempt", 3: "Disgust",
              4: "Fear", 5: "Happy", 6: "Sadness", 7: "Surprise"}
  classify = joblib.load("trained_emotions/traindata.pkl")
  pca = joblib.load("trained_emotions/pcadata.pkl")

  feature_points = detect_feature(img)
  landmarks = np.array(feature_points)

  import pdb; pdb.set_trace()
  features = generateFeatures(landmarks)
  features = np.asarray(features)
  pca_features = pca.transform(features)
  emo_predicts = classify.predict(pca_features)
  print "Predicted emotion using trained data is { " + emotions[int(emo_predicts[0])] + " }"
  emotion = int(emo_predicts[0])
  return emotion

if __name__ == '__main__':
  img = cv2.imread('report_pics/mr_robot1.jpg')
  emotion = detect_mood(img)