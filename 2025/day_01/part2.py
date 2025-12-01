dial = 50
count = 0

for line in read():
    if not line:
        continue
    direction = -1 if line[0] == 'L' else 1
    val = int(line[1:])
    if direction == -1:
        next_0 = dial or 100
    else:
        next_0 = 100 - dial
    dial = (dial + direction*val)%100
    if val >= next_0:
        count += (1 + (val - next_0) // 100)
print(count)
