import csv
import collections
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(color_codes=True)

diagnosis = collections.Counter()
with open('train/train2.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        diagnosis[row[1]] += 1

print('Number of severe cases (4): %s' % diagnosis['4'])
print(diagnosis.most_common())
dg = pd.read_csv('train/train2.csv')

df = pd.DataFrame(dict(x=dg['diagnosis']))
ax = sns.barplot(x="x", y="x", data=df, estimator=lambda x: (len(x) / len(df) *100))
ax.set(ylabel="Percent")

ax.set_title('Severity of Diabetic Retinopathy')
ax.set_ylabel('Count')
ax.set(xlabel=None)

for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    ax.annotate(f'{height/100:.2%}', (x + width/2, y + height*1.02), ha='center')
dg.info()
plt.show()