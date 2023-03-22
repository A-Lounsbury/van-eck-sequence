# van_eck_sequence.py
# Andrew Lounsbury
# 20/3/23
# generate the Van Eck sequence; https://www.youtube.com/watch?v=etMJxB-igrc

sequence = [0]

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
def generate(sequence, n):
    while len(sequence) < n:
        subsequence = sequence[:len(sequence) - 1]
        if sequence[len(sequence) - 1] in subsequence:
            sequence.append(last_seen(sequence, sequence[len(sequence) - 1]))
        else:
            sequence.append(0)
          
generate(sequence, 100)
print(sequence)