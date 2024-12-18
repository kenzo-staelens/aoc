import re
from pprint import pprint

w = 101
h = 103

seconds = 100

with open('input.txt', 'r') as f:
    expr = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    inp = re.findall(expr, f.read())

robots = []

for x,y,vx,vy in inp:
    new_x = (int(x)+seconds*(w+int(vx)))%w
    new_y = (int(y)+seconds*(h+int(vy)))%h

    robots.append((new_x, new_y))

grid = [[0 for _ in range(w)] for _ in range(h)]

count = 1
for robot in robots:
    grid[robot[1]][robot[0]] +=1

for qx, qy in [(0,0),(0,1),(1,0),(1,1)]:
    qc = 0
    for y in range(h//2):
        for x in range(w//2):
            v = grid[qy*(h//2+1)+y][qx*(w//2+1)+x]
            qc += v
    count*=qc
print(count)
