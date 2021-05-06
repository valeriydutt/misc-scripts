# misc-scripts
 A collection of various useful scripts I have written to help with different tasks.

## Restructure custom image dataset from CVS file labels to subdirectories
When using ML libraries such as keras, functions like flow_from_directory() require the dataset to be sorted into relevant sub-directories.

This script takes the dataset and its CSV file and constructs relevant directories according to the labels found in the CSV file and moves the respective files to those subdirectories, simplifying the process of importing a custom dataset.

## Filenames into a CSV file
 Parses the directory and puts all the file names into a CSV file column.

## Dataset Mean and STD
Calculates the mean and standard deviation values for a given dataset (ML utility script).

## Column Counter
Produces a bar plot with data distribution of a given dataset.

