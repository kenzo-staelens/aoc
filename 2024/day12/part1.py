visited=set()
grid=[]
areas={}
for l in inp.strip().split("\n"):
    grid.append(list(l))
    
from pprint import pprint

def find_area(x,y, find, root):
    if (x,y,find) in visited:
        return 1
    if x<0 or y<0 or x>len(grid[0])-1 or y>len(grid)-1:
        return 0
    if grid[y][x]==find:
        visited.add((x,y, find))
        areas[root] = [areas.get(root,[0])[0]+1, areas.get(root,[0,0])[1]]
        p=0
        p+=find_area(x+1,y,find,root)
        p+=find_area(x-1,y,find,root)
        p+=find_area(x,y-1,find,root)
        p+=find_area(x,y+1,find,root)
        areas[root][1]+=4-p
        return 1
    return 0
    
for x in range(len(grid[0])):
    for y in range(len(grid)):
        a=(x,y,grid[y][x])
        find_area(*a,a)

print(sum(x*y for x,y in areas.values()))
