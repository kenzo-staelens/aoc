import sys
sys.setrecursionlimit(140*140*4)

#parsing into [[...],...]
with open ("input.txt","r") as f:
    L = f.read().strip().split('\n')

grid = [list(i) for i in L]

# find s
s=(-1,-1)
for y,row in enumerate(grid):
    for x,token in enumerate(row):
        if token == "S":
            s=(y,x)
            break
    if s != (-1,-1):
        break

if s==(-1,-1):
    raise RuntimeError('S not found')

pipes={#in out mapping
    ((-1,0),"|"):(1,0),
    ((1,0),"|"):(-1,0),
    ((0,-1),"-"):(0,1),
    ((0,1),"-"):(0,-1),
    ((-1,0),"L"):(0,1),
    ((0,1),"L"):(-1,0),
    ((-1,0),"J"):(0,-1),
    ((0,-1),"J"):(-1,0),
    ((1,0),"7"):(0,-1),
    ((0,-1),"7"):(1,0),
    ((1,0),"F"):(0,1),
    ((0,1),"F"):(1,0)
}

#find a surrounding connected pipe
if grid[s[0]-1][s[1]] in "|F7":
    p1=(s[0]-1,s[1])
    p1_from = (1,0)
elif grid[s[0]+1][s[1]] in "|JL":
    p1=(s[0]+1,s[1])
    p1_from = (-1,0)
elif grid[s[0]][s[1]-1] in "-FL":
    p1=(s[0],s[1]-1)
    p1_from=(0,1)
elif grid[s[0]][s[1]+1] in "-J7":
    p1=(s[0],s[1]+1)
    p1_from=(0,-1)

c=1

#cleanup non relevant pipes, expanded for floodfill
copy = [["." for _ in range(len(grid[0])+2)] for i in range(len(grid)+2)]

while True:
    p1_sym = grid[p1[0]][p1[1]]
    if p1_sym=="S":
        copy[s[0]+1][s[1]+1]="S"
        break
    temp = pipes[(p1_from,p1_sym)]
    copy[p1[0]+1][p1[1]+1]=grid[p1[0]][p1[1]]
    p1=(p1[0]+temp[0],p1[1]+temp[1])
    p1_from=(-temp[0],-temp[1])
    c+=1

#note: figure out S equivalence

newgrid =[]
for row in copy:
    nr1 = []
    nr2 = []
    for sym in row:
        if sym == "S":
            nr1+=["x","x"]
            nr2+=["x","x"]
        elif sym == "|" or sym=="7":
            nr1+=["x","."]
            nr2+=["x","."]
        elif sym == "-" or sym=="L":
            nr1+=["x","x"]
            nr2+=[".","."]
        elif sym=="F":
            nr1+=["x","x"]
            nr2+=["x","."]
        elif sym=="J":
            nr1+=["x","."]
            nr2+=[".","."]
        else:
            nr1+=[".","."]
            nr2+=[".","."]
    newgrid.append(nr1)
    newgrid.append(nr2)

#floodfill from 0,0
def floodfill(y,x,step,find,set):
    if y<0 or x<0 or y>=len(newgrid) or x>=len(newgrid[0]):
        return
    if newgrid[y][x]==find:
        newgrid[y][x]=set
        newgrid[y+step-1][x]=set
        newgrid[y][x+step-1]=set
        newgrid[y+step-1][x+step-1]=set
        floodfill(y+step,x,step,find,set)
        floodfill(y,x+step,step,find,set)
        floodfill(y-step,x,step,find,set)
        floodfill(y,x-step,step,find,set)
floodfill(0,0,1,".","f")
floodfill((s[0]+1)*2,(s[1]+1)*2,2,"x","w")

#count "."
c2=0
for r in newgrid[::2]:
    for s in r[::2]:
        if s==".":
            c2+=1
print("part1: ",c/2)
print("part2: ",c2)
