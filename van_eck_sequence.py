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

n = 1000
sequence = generate_van_eck(n)
df1 = pd.DataFrame(sequence, columns = ["Number"])

indices = []
for i in range(n):
    indices.append(i)
    
df1['index'] = indices
sns.scatterplot(x="index", y="Number", data=df1)
plt.show()

n = 10000
sequence = generate_van_eck(n)
df2 = pd.DataFrame(sequence, columns = ["Number"])

indices = []
for i in range(n):
    indices.append(i)
    
df2['index'] = indices
sns.scatterplot(x="index", y="Number", data=df2)
plt.show()

n = 100000
sequence = generate_van_eck(n)
df3 = pd.DataFrame(sequence, columns = ["Number"])

indices = []
for i in range(n):
    indices.append(i)
    
df3['index'] = indices
sns.scatterplot(x="index", y="Number", data=df3)
plt.show()