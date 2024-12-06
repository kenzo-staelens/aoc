from pprint import pprint

grid = []
x,y = 0,0

with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        grid.append(list(line.strip()))
        if '^' in line:
            y = i
            x = line.index('^')
rotation_map = {'^':'>','>':'v', 'v':'<','<':'^'}
step_map = {
    '^': [0,-1],
    '>': [1,0],
    'v': [0,1],
    '<': [-1,0],
}
def step():
    global x
    global y
    global grid
    dx, dy = step_map[grid[y][x]]
    if y+dy <0 or x+dx<0:
        raise IndexError("done")
    if grid[y+dy][x+dx]!='#':
        grid[y+dy][x+dx]=grid[y][x]
        grid[y][x]='x'
        x,y = x+dx, y+dy
    else:
        grid[y][x] = rotation_map[grid[y][x]]
try:
    while True:
        step()
except IndexError as e:
    pass
count=0
for line in grid:
    print(''.join(line))
    for char in line:
        if char=='x':
            count+=1
print(count+1) # off by one error
