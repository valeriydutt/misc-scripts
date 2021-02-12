import os
import csv

data=[]
with open('images.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    for filename in os.listdir("data"):

        # Remove last 5 characters from filename, in this case .jpeg
        data.append(filename[:-5])
        writer.writerow(data)
        data=[]
writeFile.close()