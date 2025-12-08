import math
boxes = []
for line in read(strip = True):
    x,y,z = line.split(',')
    x,y,z = int(x),int(y),int(z)
    boxes.append((x,y,z))

def distance(a,b):
    metric = 0
    for va, vb in zip(a,b, strict=True):
        metric += (vb-va)**2
    return math.sqrt(metric)

distances = []
pairs = set()

# distance metrics:
for i, a in enumerate(boxes):
    for j, b in enumerate(boxes):
        if i==j or (j, i) in pairs:
            continue
        distances.append((i, j, distance(a,b)))
        pairs.add((i,j))

distances.sort(key = lambda v: v[2])


circuits = [set((i, )) for i in range(len(boxes))]
new_circuits = []
joining = set()
connections = 0
i = 0
while connections < 1000:
    box1, box2, _  = distances[i]
    for circuit in circuits:
        if box1 in circuit or box2 in circuit:
            joining |= circuit
        else:
            new_circuits.append(circuit)
    new_circuits.append(joining)
    circuits = new_circuits
    new_circuits = []
    joining = set()
    i += 1
    connections += 1

import math
tail = sorted([len(x) for x in circuits])
print(math.prod(tail[-3:]))