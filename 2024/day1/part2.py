a, b = {}, {}

with open("input.txt", 'r') as f:
    for line in f.readlines():
        A, B = line.split()
        A, B = int(A), int(B)
        if A in a:
            a[A] +=1
        else:
            a[A] = 1
        if B in b:
            b[B] +=1
        else:
            b[B] = 1


similarity = 0
for k, v in a.items():
    val = k*v*b.get(k, 0)
    print("k, v, val, sim")
    print(k, v, val, similarity)
    print("simval", similarity+val)
    similarity+=val


print(similarity)
