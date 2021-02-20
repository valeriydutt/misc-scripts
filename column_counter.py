import csv
import collections
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(color_codes=True)

diagnosis = collections.Counter()
with open('train/train.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        diagnosis[row[1]] += 1

print('Number of severe cases (4): %s' % diagnosis['4'])
print(diagnosis.most_common())

dg = pd.read_csv('train/train.csv')
ax = sns.countplot(x=dg['diagnosis'])
ax.set_title('Severity of diabetic Retinopathy')
ax.set_ylabel('Count')
ax.set(xlabel=None)

dg.info()
plt.show()