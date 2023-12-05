from range_intersect import divide

def create_seed_ranges(iterable):
    l = []
    for x in range(0,len(iterable),2):
        l.append((iterable[x],iterable[x]+iterable[x+1]-2))
    return l

def convert_map(map_item):
    return [convert_map_line(line) for line in map_item]

def convert_map_line(line):
    dst, src, l = [int(x) for x in line.split()]
    linerange = (src, src+l-1)
    return [linerange, dst]

def map_intersect(mapping, intersect):
    mapping_range = mapping[0]
    diff_lower = intersect[0]-mapping_range[0]
    intersect_len = intersect[1]-intersect[0]
    retval = (mapping[1]+diff_lower,mapping[1]+diff_lower+intersect_len)
    return retval

def process_map_seeds(map,seeds, edgecases):
    ranges = []
    while len(seeds)>0:
        item = seeds.pop(0)
        len_before = len(ranges)
        for mapping in map:
            lower, intersect, upper = divide(item, mapping[0])
            if intersect==tuple():
                # no intersect found yet: cannot map
                continue
            ranges.append(map_intersect(mapping,intersect))
            if intersect[0]==item[0] and intersect[1] == item[1]:
                #full intersect
                break
            if edgecases:
                #always discard empty lower and upper
                if upper != tuple() and upper[1]==item[1]:
                    seeds.append(upper) #continue processing rest
                elif lower !=tuple() and lower[0]==item[0]:
                    seeds.append(lower) #continue processing rest
        if len_before == len(ranges):
            ranges.append(item) # no mapping found
    return ranges

with open("input.txt","r") as f:
    input = f.read()

maps = input.split("\n\n") #split large sections
seeds = create_seed_ranges([int(x) for x in maps.pop(0).split(": ")[1].split(" ")])
maps = [x.split("\n")[1:] for x in maps] #split into lines, cut head

def run(edgecase):
    seedlist = [x for x in seeds] # copy for destructive operation
    for map_item in maps:
        seedlist = process_map_seeds(convert_map(map_item), seedlist,edgecase)
    print(min([item[0] for item in seedlist]))

run(False)
