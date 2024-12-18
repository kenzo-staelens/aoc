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
        areas[root] = [areas.get(root,[0])[0]+1, areas.get(root,[0,0])[1],areas.get(root,[0,0,[]])[2]]
        areas[root][2].append((x,y))
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

print(sum(x*y for x,y,_ in areas.values()))

def tiny_map(nodes):
    map=[[0 for _ in grid[0]] for _ in grid]
    for node in nodes:
        map[node[1]][node[0]]=1

    map = [line for line in map if any(x != 0 for x in line)]
    trim_min = 0
    trim_max= 0
    for i in range(len(map[0])):
        if any(map[x][i]==1 for x in range(len(map))):
            break
        trim_min+=1
    trim_max=trim_min+1
    for i in range(trim_max,len(map[0])):
        if all(map[x][i]==0 for x in range(len(map))):
            break
        trim_max+=1
    
    map = [[0]+line[trim_min:trim_max]+[0] for line in map]
    zp = [0]*len(map[0])
    map.insert(0,zp)
    map.append(zp)
    return map

def count_edge(map):
    count=0
    for i in range(len(map)-2):
        toggle=False
        for j in range(len(map[0])):
            if map[i][j]==0 and map[i+1][j]==1:
                if not toggle:
                    toggle=True
                    count+=1
            else:
                toggle= False
    return count

def transpose(m):
    nm =[]
    for i in range(len(m[0])):
        l=[]
        for j in range(len(m)):
            l.append(m[j][i])
        nm.append(l)
    return nm
            
def mirror(m):
    return m[::-1]

def get_edges(tm):
    c = count_edge(tm)
    tm=mirror(tm)
    c+=count_edge(tm)
    tm = transpose(tm)
    c+=count_edge(tm)
    tm= mirror(tm)
    c+=count_edge(tm)
    return c

count=0
for item in areas.values():
   # print(item)
   tm = tiny_map(item[2])
   count+=get_edges(tm)*item[0]

print(count)
