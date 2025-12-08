init_ranges = []
for line in read():
    if not line.strip():
        break

    # update ranges if intersect
    a,b = line.strip().split('-')
    a,b = int(a), int(b)
    init_ranges.append((a,b))


def update_intersects(a,b, ranges):
    for i, (min_r, max_r) in enumerate(ranges):
        if a>=min_r and b<=max_r:
            # fully consumed
            break
        if a<=min_r and min_r<=b<=max_r:
            ranges[i] = (a, max_r)
            break
        if min_r<=a<=max_r and b>max_r:
            ranges[i] = (min_r, b)
            break
        if a<min_r and b>max_r:
            ranges[i] = (a,b)
            break
    else:
        ranges.append((a,b))

ranges = init_ranges
i=0
while i==0 or len(ranges)!=len(init_ranges):
    init_ranges = ranges
    ranges = []
    for a,b in init_ranges:
        update_intersects(a,b, ranges)
    i+=1
fresh = 0
for a,b in ranges:
    fresh += b-a+1
print(fresh)
print(f"used {i} refinement steps")
