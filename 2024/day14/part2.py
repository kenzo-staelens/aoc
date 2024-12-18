import re
from pprint import pprint

w = 101
h = 103

seconds = 100

with open('input.txt', 'r') as f:
    expr = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    inp = re.findall(expr, f.read())


def printimage(robots):
    grid = [[False for _ in range(w)] for _ in range(h)]
    for robot in robots:
        grid[robot[1]][robot[0]] = True
    for y in range(h):
        for x in range(w):
            if grid[y][x]:
                print('#', end='')
            else:
                print(' ', end='')
        print()


inp = [[int(x) for x in r] for r in inp]
found = set()
seconds = 1
while True:
    inp = tuple(((robot[0]+robot[2]+w)%w, (robot[0]+robot[3]+h)%h, robot[2],robot[3]) for robot in inp)
    if inp in found:
        break
    found.add(inp)
    print(f"{seconds=}")
    printimage(inp)
    input()
    seconds+=1
