import csv
import collections

diagnosis = collections.Counter()
with open('train/train.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        diagnosis[row[1]] += 1

print('Number of severe cases (4): %s' % diagnosis['4'])
print(diagnosis.most_common())