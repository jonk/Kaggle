from scipy import ndimage
import numpy as np
import os
import csv

kaggleFolder = "/Users/jonkalfayan/Documents/GitRepos/Kaggle/"
train_data = kaggleFolder + "trainResized/"
train_labels = kaggleFolder + "trainLabels.csv"
test_data = kaggleFolder + "testResized/"

x_train = []
y_train = []

x_test = []

for filename in os.listdir(train_data):
	img = train_data + filename
	img_arr = ndimage.imread(img, True)
	x_train.append(img_arr.ravel())

for filename in os.listdir(test_data):
    img = test_data + filename
    img_arr = ndimage.imread(img, True)
    x_test.append(img_arr.ravel())

x_test = np.matrix(x_test)
x_train = np.matrix(x_train)

with open(train_labels, 'rb') as f:
    reader = csv.reader(f)
    y_train = list(reader)
y_train.pop(0)

predictions = []
k = 1

def kNN():
    pass

def squaredDist(p1, p2):
	return np.dot(np.subtract(p1, p2), np.subtract(p1, p2).T)

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
		neighbors.append(y_train[leastDist][1])
		neighborDists.remove(min(neighborDists))
	return findMaxLabel(neighbors)

print findNearestNeighborsLabel(x_test[0], k)




