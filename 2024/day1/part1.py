a, b = [], []

with open("input.txt", 'r') as f:
    for line in f.readlines():
        A, B = line.split()
        a.append(int(A))
        b.append(int(B))


a.sort()
b.sort()
summed = 0
for A, B in zip(a, b):
    summed += abs(A-B)


print(summed)
