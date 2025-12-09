corners = []

for line in read(strip=True):
    a,b = line.split(',')
    corners.append((int(a), int(b)))

import itertools
unsorted = []
for c1, c2 in itertools.combinations(corners, 2):
    x1, y1 = c1
    x2, y2 = c2
    size = (abs(x1-x2)+1)*(abs(y1-y2)+1)
    unsorted.append((c1, c2, size))

unsorted.sort(key=lambda v: v[2])
print(unsorted[-1])
