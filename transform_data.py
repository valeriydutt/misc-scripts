import pandas as pd
import os
import numpy as np
import shutil

"""
Initialize the CSV name

Ensure that the column names are matching the CSV

"""
dataset = pd.read_csv('trainLabels.csv')
file_names = list(dataset['image'].values)
img_labels = list(dataset['level'].values)

# Checks the labels data for unique values to create corresponding folders
folders_to_be_created = np.unique(list(dataset['level'].values))

source = os.getcwd()

for new_path in folders_to_be_created:
    if not os.path.exists(".//" + str(new_path)):
        os.makedirs(str(new_path))

# Ensure that nothing besides the data files, csv, and this script are in the directory
folders = folders_to_be_created.copy()

"""
For each entry in the csv file:
1. find its corresponding name and label
2. move the file from current dir to its respective label dir
"""
print(len(file_names))
for f in range(len(file_names)):

  current_img = file_names[f]
  current_label = img_labels[f]

  # Change this line accordingly, check file extension
  shutil.move(current_img + ".jpeg", str(current_label))