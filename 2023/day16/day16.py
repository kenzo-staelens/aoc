import re
with open ("input.txt","r") as f:
    inp = f.read().strip().split("\n")

import sys
sys.setrecursionlimit(int(1e9))

hits=None
new=None #lightray table

#super dirty recursive solver
def right(x,y):
    if x<0 or y<0 or x>=len(inp[y-1]) or y<0 or y>=len(inp):
        return
    new[y][x]="#"
    if (x,y,">") in hits:
        return #already done
    if inp[y][x] in "\\/|-":
        #value irrelevant
        hits[(x,y,">")]=None
    if inp[y][x] in ["\\","|"]:
        down(x,y+1)
    if inp[y][x] in ["/","|"]:
        up(x,y-1)
    if inp[y][x] in [".","-"]:
        right(x+1,y)

def left(x,y):
    if x<0 or y<0 or x>=len(inp[y-1]) or y>=len(inp):
        return
    new[y][x]="#"
    if (x,y,"<") in hits:
        return #already done
    if inp[y][x] in "\\/|-":
        #value irrelevant
        hits[(x,y,"<")]=None
    if inp[y][x] in ["\\","|"]:
        up(x,y-1)
    if inp[y][x] in ["/","|"]:
        down(x,y+1)
    if inp[y][x] in [".","-"]:
        left(x-1,y)

def up(x,y):
    if x<0 or y<0 or x>=len(inp[y-1]) or y>=len(inp):
        return
    new[y][x]="#"
    if (x,y,"^") in hits:
        return #already done
    if inp[y][x] in "\\/|-":
        #value irrelevant
        hits[(x,y,"^")]=None
    if inp[y][x] in ["\\","-"]:
        left(x-1,y)
    if inp[y][x] in ["/","-"]:
        right(x+1,y)
    if inp[y][x] in [".","|"]:
        up(x,y-1)

def down(x,y):
    if x<0 or y<0 or x>=len(inp[y-1]) or y>=len(inp):
        return
    new[y][x]="#"
    if (x,y,"v") in hits:
        return #already done
    if inp[y][x] in "\\/|-":
        #value irrelevant
        hits[(x,y,"v")]=None
    if inp[y][x] in ["\\","-"]:
        right(x+1,y)
    if inp[y][x] in["/","-"]:
        left(x-1,y)
    if inp[y][x] in [".","|"]:
        down(x,y+1)

def p(*args):
    #print the light table
    #with any extra info
    print(*args)
    print("\n".join(["".join(x) for x in new]))
    print()

def solve_for(f,x,y):
    #init vars
    global new
    global hits
    hits={}
    new = [["." for _ in inp[0]] for _ in inp]
    #solve with *function(x,y)*
    #with f = 1 of recursive solver
    f(x,y)
    # count "#"
    sum=0
    for i in new:
        for j in i:
            if j=="#":
                sum+=1
    return sum

#find maximum config
max = 0
store=None
for row in range(-1,len(inp)+1):
    s=solve_for(right,0,row)
    if s>=max:
        max=s
        store=("right",0,row)
    s=solve_for(left,len(inp[0])-1,row)
    if s>=max:
        max=s
        store=("left",len(inp[0])-1,row)


for col in range(-1,len(inp[0])+1):
    s=solve_for(down,col,0)
    if s>=max:
        max=s
        store=("down",col,0)
    s=solve_for(up,col,len(inp)-1)
    if s>=max:
        max=s
        store=("up",col,len(inp)-1)

#print("\n".join(inp))
print("part1:",solve_for(right,0,0))
print("part2:",max,store)
