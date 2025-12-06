import numpy as np
import math

arr = []
ops = []
for line in read(strip=True):
    if '+' in line:
        ops = line.split()
        continue
    arr.append([int(x) for x in line.split()])

arr = np.array(arr)
sums = sum(arr)
mults = math.prod(arr)
ops = np.array(ops)
op_plus = (ops == '+').astype(int)

print(sum(sums*op_plus + (1-op_plus)*mults))