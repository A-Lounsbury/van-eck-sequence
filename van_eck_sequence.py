# van_eck_sequence.py
# Andrew Lounsbury
# 20/3/23
# generate the Van Eck sequence; https://www.youtube.com/watch?v=etMJxB-igrc

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# computes the last time a number appeared in the sequence
def last_seen(sequence, num):
    sequence.reverse()
    pos = 0
    if len(sequence) == 1 and num == 0:
        return 0
    else:
        curNum = sequence[pos]
        firstFound = False
        while curNum != num or not firstFound:
            pos += 1
            curNum = sequence[pos]
            if curNum == num:
                firstFound = True
    sequence.reverse()
    return pos

# generates the sequence up to the n-th number
def generate_van_eck(n):
    sequence = [0]
    while len(sequence) < n:
        subsequence = sequence[:len(sequence) - 1]
        if sequence[len(sequence) - 1] in subsequence:
            sequence.append(last_seen(sequence, sequence[len(sequence) - 1]))
        else:
            sequence.append(0)
    return sequence
          
sequence = generate_van_eck(100)
print(sequence)

# Basic Scatterplots
# n = 100
# sequence = generate_van_eck(n)
# df = pd.DataFrame(sequence, columns = ["Number"])
# df['index'] = [i for i in range(n)]
# sns.scatterplot(x="index", y="Number", data=df)
# plt.savefig("images/100.png")
# plt.show()

# n = 1000
# sequence = generate_van_eck(n)
# df = pd.DataFrame(sequence, columns = ["Number"])
# df['index'] = [i for i in range(n)]
# sns.scatterplot(x="index", y="Number", data=df)
# plt.savefig("images/1000.png")
# plt.show()

# n = 10000
# sequence = generate_van_eck(n)
# df = pd.DataFrame(sequence, columns = ["Number"])
# df['index'] = [i for i in range(n)]
# sns.scatterplot(x="index", y="Number", data=df)
# plt.savefig("images/10000.png")
# plt.show()

# n = 100000
# sequence = generate_van_eck(n)
# df = pd.DataFrame(sequence, columns = ["Number"])
# df['index'] = [i for i in range(n)]
# sns.scatterplot(x="index", y="Number", data=df)
# plt.savefig("images/100000.png")
# plt.show()

# Averages
n = 10
sequence = generate_van_eck(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_average)
plt.savefig("images/average_10.png")
plt.show()

n = 100
sequence = generate_van_eck(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_average)
plt.savefig("images/average_100.png")
plt.show()

n = 1000
sequence = generate_van_eck(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_average)
plt.savefig("images/average_1000.png")
plt.show()

n = 10000
sequence = generate_van_eck(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_average)
plt.savefig("images/average_10000.png")
plt.show()

n = 100000
sequence = generate_van_eck(n)
average_sequence = []
sum = 0
for i, s in enumerate(sequence):
    sum += s
    average = sum / (i + 1)
    average_sequence.append(average)
    
df_average = pd.DataFrame(average_sequence, columns=["Average"])
df_average['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Average", data=df_average)
plt.savefig("images/average_100000.png")
plt.show()