# part 2 is a DP problem
last = {}
current = {}
splits = 0
print()
for l, line in enumerate(read(strip=True)):
    if l%2:
        continue
    for i, value in enumerate(line):
        if value == 'S':
            current[i] = 1
        if value == '.' and i in last:
            current[i] = current.get(i, 0) + last.get(i, 0)
        if value == '^' and i in last:
            # no splitters exist at edges 
            # -> no bounds check needed
            current[i-1] = current.get(i-1, 0) + last.get(i)
            current[i+1] = current.get(i+1, 0) + last.get(i)
    last, current = current, {}
print(sum(last.values()))