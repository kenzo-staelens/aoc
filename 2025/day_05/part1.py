mode = 0 # fresh list = 0; ingredients = 1
ranges = []
ingredients = []
for line in read():
    if not line.strip():
        mode = 1
        continue
    if mode == 0:
        a,b = line.strip().split("-")
        ranges.append((int(a), int(b)))
    else:
        ingredients.append(int(line))

fresh = 0
for ingredient in ingredients:
    for min_r, max_r in  ranges:
        if min_r <= ingredient <= max_r:
            fresh += 1
            break
print(fresh)
