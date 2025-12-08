
last = set()
current = set()
splits = 0
for line in read(strip=True):
    for i, value in enumerate(line):
        if value == 'S' or value == '.' and i in last:
            current.add(i)
        if value == '^' and i in last:
            # no splitters exist at edges 
            # -> no bounds check needed
            current.add(i-1)
            current.add(i+1)
    splits += len(last - current)
    last, current = current, set()
print(splits)