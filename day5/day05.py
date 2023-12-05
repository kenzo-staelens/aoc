def parsemap(map,seed):
    for line in map:
        if line=="":
            continue
        flag, val = parseline(line,seed)
        if flag:
            return val
    return seed

def parseline(line, seed):
    dst, src, l = [int(x) for x in line.split()]
    if seed>=src and seed<src+l:
        diff = seed - src
        return True, dst+diff
    return False, seed

with open("sample.txt","r") as f:
    input = f.read()

maps = input.split("\n\n")
seeds = [int(x) for x in maps.pop(0).split(": ")[1].split(" ")]


def part_2_naive(iterable):
    global seeds
    seeds = []
    for x in range(0,len(iterable),2):
        for item in range(iterable[x],iterable[x]+ iterable[x+1]+1):
            seeds.append(item)
            # yield item
    return seeds
# part_2_naive(seeds)

maps = [x.split("\n")[1:] for x in maps]
for map in maps:
    seeds = [parsemap(map,seed) for seed in seeds]

print(min(seeds))