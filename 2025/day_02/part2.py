import re
line = next(read())

def find_pattern(min_val, max_val, cutoff=2):
    dups = 0
    # and here i was expecting much larger ranges but too lazy solve p2 like p1
    for i in range(int(min_val), int(max_val)+1):
        matched = re.match(r'(^(\d+)\2+$)', str(i))
        if matched:
            dups += int(matched.groups()[0])
    return dups
i=0
d = 0

for item in line.split(','):
    a,b = item.split('-')
    dups = find_pattern(a,b)
    d+= dups
print(d)
