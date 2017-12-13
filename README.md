# Face_Swapping

##Basic skeleton

*function video_loader(file_path,len_frame,size=(H,W))*
input: 
	file_path: the path of the avi file
	len_frame: int 
	output_img_size,H,W: int,int
output: a list of images



*function feature_detect(img)*
input: 
	image WxHx3 
output: 
	points: an list of face feature * 5 [[x1,y1],[x2,y2],[x3,y3]] 
NOTE: order of points matters,x1,y1 are coordinate

*function extract_mask(points,(H,W))*
input: 
	points: list of points
output: 
	mask: an HxW boolean matrics reprenst the mask
NOTE: using: scipy.spatial.ConvexHull to calculate the boundary

*function estimate_homography(points_source,points_target)*
input: 
	points_source: list of points
	points_target: list of points
output: 
	H: homography matrix represent how to transform image from source to target
NOTE: only use the convex hull point to estimate homography so that we can put the emotion of source image appear on the target body without be influenced

*function blending(img_source, img_target,mask,H)*
input:
	img_source: WxHx3 
	img_target: WxHx3 
	mask: WxH
	H: homography matrix
output:
	img: WxHx3, the image after
NODE: we may use the seamless clone to make it more natural
```
output = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
```