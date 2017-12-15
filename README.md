# Face_Swapping

## Basic skeleton
```
function video_loader(file_path_s, file_path_t ,len_frame,file_output_path)
```
input: 
	file_path_s: the path of the mp4 file of source  
	file_path_t: the path of the mp4 file of target  
	len_frame: int  
	file_output_path: the path of output videooutput: a list of images  

```
function feature_detect(img)
```
input: 
	image WxHx3 
	
output: 
	points_in_pic: an list of person's face feature in img each one contains 68 * 2 dimension (total n * 68 * 2)
	
NOTE: order of points matters, 0th ~ 26th is the contour of the face 

```
function extract_mask(points,(H,W))
```
input: 
	points: list of points
	
output: 
	mask: an HxW boolean matrics reprenst the mask
	
NOTE:  
* scipy.spatial.ConvexHull to calculate the boundary

```
function estimate_homography(points_source,points_target)
```
input: 
	points_source: list of points
	points_target: list of points

output: 
	H: homography matrix represent how to transform image from source to target

NOTE: only use the convex hull point to estimate homography so that we can put the emotion of source image appear on the target body without be influenced

```
function blending(img_source, img_target,mask,H)
```
input:
	img_source: WxHx3 
	img_target: WxHx3 
	mask: WxH
	H: homography matrix

output:
	img: WxHx3, the image after

NODE: we may use the seamless clone to make it more natural

* output = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE) 
