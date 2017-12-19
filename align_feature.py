from packages import *
from functions import *

# eyebrows, eyes, nose, mouth, jaw and face to create affine transformation matrix
ALIGNMENT_REGIONS = list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42))+list(range(27, 35))+list(range(48, 61))

# eyebrows, eyes, nose and mouth to create feature mask
OVERLAY_REGIONS = [list(range(22, 27))+list(range(17, 22))+list(range(42, 48))+list(range(36, 42)), list(range(27, 35))+list(range(48, 61))]

# feature overlay using Ordinary Procrustes analysis
def align_feature(source_pts, target_pts):