import functools
with open("input.txt","r") as f:
    input = tuple(f.read().strip().split("\n"))

def transpose(lines):
    return tuple(list(x) for x in zip(*lines))

def mirror_v(lines):
    return lines[::-1]

def mirror_h(lines):
    return tuple(line[::-1] for line in lines)

def calc_part_1_line(line,length):
    sum = 0
    rock_at=length
    for i,item in enumerate(line):
        if item=="#":
            rock_at=length-1-i
            continue
        if item=="O":
            sum+=rock_at
            rock_at-=1
    return sum

def update_line_p2(line,length):
    rock_at=0
    result_str = ["."]*length
    for i,item in enumerate(line):
        if item=="#":
            result_str[i]=item
            rock_at=i+1
            continue
        if item=="O":
            result_str[rock_at]=item
            rock_at+=1
    return "".join(result_str)

def p1_calc_alt(line):
    #fuq's wrong with the other part1 calc
    # somehow gives wrong result on cycles, this one doesn't
    c=0
    for i in line:
        if i=="O":
            c+=1
    return c

def part1(inp):
    sum=0
    weight= len(inp[0])
    for i in inp:
        # c=calc_part_1_line(i,l)
        calc =p1_calc_alt(i)*weight
        weight-=1
        sum+=calc
        # print('--',calc, c, weight,i)
    return sum

@functools.lru_cache()
def part_2_cycle(inp,transform):
    #transform to implementation
    if transform=="N":
        inp = transpose(inp)
    if transform=="E":
        inp = mirror_h(inp)
    if transform=="S":
        inp=transpose(mirror_v(inp))
    inp = tuple(update_line_p2(line,len(line)) for line in inp)
    #reset input to correct orientation
    if transform=="N":
        inp = transpose(inp)
    if transform=="E":
        inp = mirror_h(inp)
    if transform=="S":
        inp=mirror_v(transpose(inp))
    return tuple("".join(x) for x in inp)

x= part_2_cycle(input,"N")
print("part1: ",part1(x))

@functools.lru_cache()
def complete_cycle(inp):
    inp = part_2_cycle(inp,"N")
    inp = part_2_cycle(inp,"W")
    inp = part_2_cycle(inp,"S")
    inp = part_2_cycle(inp,"E")
    return inp

@functools.lru_cache() # memoize large chunks of iteration
def partial_lru(inp,cycles):
    for _ in range(cycles):
        inp = complete_cycle(inp)
    return inp

partial_size = 1000
# total_cycles=1000_000_000#1e9
total_cycles=1e9

for i in range(int(total_cycles/partial_size)):
    input= partial_lru(input,partial_size)
print("part2: ", part1(input)) #load after cycles