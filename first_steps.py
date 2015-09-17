from scipy import ndimage
import numpy as np
import os
import csv

kaggleFolder = "/Users/jonkalfayan/Documents/GitRepos/Kaggle/"
train_data = kaggleFolder + "trainResized/"
train_labels = kaggleFolder + "trainLabels.csv"

x_train = []
y_train = []

for filename in os.listdir(train_data):
	img = train_data + filename
	img_arr = ndimage.imread(img, True)
	x_train.append(img_arr.ravel())

x_train = np.matrix(x_train)

with open(train_labels, 'rb') as f:
    reader = csv.reader(f)
    y_train = list(reader)

y_train.pop(0)

print y_train[0]













def findMaxLabel(neighbors):
	helper_dict = dict()
	for neighbor in neighbors:
		if neighbor in helper_dict:
			helper_dict[neighbor] += 1
		else:
			helper_dict[neighbor] = 1
	return max(helper_dict.iterkeys(), key=(lambda key: helper_dict[key]))


def findNearestNeighborsLabel(img, k):
	neighborDists = []
	for train_img in x_train:
		dist = squaredDist(img, train_img)
		neighborDists.append(dist)
	neighbors = []
	for j in range(k):
		leastDist = neighborDists.index(min(neighborDists))
		neighbors.append(y_train[leastDist])
		neighborDists.remove(min(neighborsDists))
	return findMaxLabel(neighbors)

			
	


def squaredDist(p1, p2):
	return np.dot(np.subtract(p1, p2), np.subtract(p1, p2).T)

print squaredDist(x_train[1], x_train[2])




