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

print y_train[2]


