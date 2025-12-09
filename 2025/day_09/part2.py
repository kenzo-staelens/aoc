import itertools

corners = []
for line in read(strip=True):
    a,b = line.split(',')
    a,b = int(a), int(b)
    # b/a because i'm tripping balls when handling list in my head otherwise
    corners.append((b,a))

pairs = []
for c1, c2 in itertools.combinations(corners, 2):
    x1, y1 = c1
    x2, y2 = c2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    size = (max_x - min_x +1) * (max_y - min_y + 1)
    pairs.append(((min_x+0.5, min_y+0.5), (max_x-0.5, max_y-0.5), size))

# sort from high to low
pairs.sort(key=lambda p: -p[2])

def horizontal_intersect(rect, p1, p2):
    min_x, min_y, max_x, max_y = rect
    lh, pmin, pmax = p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])
    if not (min_x < lh < max_x):
        return False
    if pmin < min_y < pmax:
        return True
    if pmin < max_y < pmax:
        return True
    return False


def vertical_intersect(rect, p1, p2):
    min_x, min_y, max_x, max_y = rect
    lv, pmin, pmax = p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])
    if not (min_y < lv < max_y):
        return False
    if pmin < min_x < pmax:
        return True
    if pmin < max_x < pmax:
        return True
    return False

corners = corners + [corners[-1]]
for (min_x, min_y), (max_x, max_y), size in pairs:
    # print((min_x, min_y), (max_x, max_y), size)
    rect = (min_x, min_y, max_x, max_y)
    meth = vertical_intersect
    valid = True
    for i in range(len(corners)-1):
        p1, p2 = corners[i], corners[i+1]
        if p1[0] == p2[0]:
            # horizontal
            meth = horizontal_intersect
        if meth(rect, p1, p2):
            valid = False
    if valid: break
for item in pairs:
    (a,b),(c,d),e = item
    a = int(a+0.5) # min x
    b = int(b+0.5) # min y
    c = int(c+0.5) # max x
    d = int(d+0.5) # max y
    print((a,b), (c,d), e)
print(rect, size, valid)
