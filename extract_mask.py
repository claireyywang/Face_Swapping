from basic_packages import * 

def extract_mask(points_list,img):
	h,w = img.shape
	for points in points_list:
		hull = ConvexHull(points)
		hull_path = Path(points[hull.vertices])
		mesh_x, mesh_y = np.meshgrid(np.arange(w),np.arange(h))
		mesh_x = mesh_x.flatten()
		mesh_y = mesh_y.flatten()
		mesh = np.asarray([mesh_x,mesh_y]).transpose()
		mask = hull_path.contains_points(mesh)
		mask = mask.reshape(h,w)
		
		# # Debug, showing the face mask
		# img_b_a = np.bitwise_and(img,mask) 
		# plt.imshow(img_b_a)
		# plt.show()
	return mask