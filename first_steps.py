from scipy import ndimage
import numpy as np
import os
import csv

kaggleFolder = "/Users/Jonk/Documents/Developer/GitRepos/Kaggle/"
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


predictions = []
k = 1

print x_test[1:2]

def kNN():
    pass
    



















def squaredDist(p1, p2):
	return np.dot(np.subtract(p1, p2), np.subtract(p1, p2).T)

print squaredDist(x_train[1], x_train[2])




