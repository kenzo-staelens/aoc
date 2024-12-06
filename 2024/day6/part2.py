from pprint import pprint

grid = []
x,y = 0,0

with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        l = line.strip()
        grid.append(list(l))
        if '^' in line:
            y = i
            x = line.index('^')
init_x, init_y, initdir = x,y,grid[y][x]

rotation_map = {'^':'>','>':'v', 'v':'<','<':'^'}

replacemap = {'^':'|','v':'|', '>':'-','<':'-'}
step_map = {
    '^': [0,-1],
    '>': [1,0],
    'v': [0,1],
    '<': [-1,0],
}

def printgrid(g):
    for line in g:
        print(''.join(line))
    print()

def step(g):
    global x
    global y
    global grid
    dx, dy = step_map[g[y][x]]
    if y+dy <0 or x+dx<0:
        raise IndexError("done")
    if g[y+dy][x+dx]!='#':
        g[y+dy][x+dx]=g[y][x]
        g[y][x]='.'
        x,y = x+dx, y+dy
    else:
        g[y][x] = rotation_map[g[y][x]]

def checkloop(g):
    path = set()
    while True:
        direction = g[y][x]
        c_x = x
        c_y = y
        try:
            step(g)
        except IndexError:
            return False
        if (x,y,direction) in path:
            return True
        path.add((c_x,c_y, direction))

def copy_grid():
    g = []
    for line in grid:
        r = []
        for item in line:
            r.append(item)
        g.append(r)
    return g

count = 0

# yes yes i know, there are optimizations like only keeping track of where you turn
# or only putting obstructions in the path but i honestly can't care, it's only a few
# thousand locations to check

for i_y in range(len(grid)):
    for i_x in range(len(grid[i_y])):
        if i_y%10==0 and i_x%10==0: # just in case shit is super slow
            print(f'y={i_y} x={i_x}')
        g = copy_grid()
        if g[i_y][i_x]=='#' or g[i_y][i_x] =='^':
            continue
        g[i_y][i_x]='#'
        r = checkloop(g)
        if r:
            count+=1
        x,y = init_x, init_y
print(count)
