import numpy as np
from scipy import ndimage, misc
import os

data_folder = "/Users/jonkalfayan/Documents/GitRepos/Other/trainResized/"

feature_mat = []

for filename in os.listdir(data_folder):
	img = data_folder + filename
	img_arr = ndimage.imread(img, True)
	feature_mat.append(img_arr.ravel())


feature_mat = np.matrix(feature_mat)


