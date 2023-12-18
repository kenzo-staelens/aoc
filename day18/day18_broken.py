import heapq
with open ("test.txt","r") as f:
    inp = f.read().strip().split("\n")

import sys
sys.setrecursionlimit(int(1e7))

dirs={"U":(0,-1),"D":(0,1),"L":(-1,0),"R":(1,0)}

suml= 0
sumr=0
sumu=0
sumd=0
for i in inp:
    num = int(i.split(" ")[1])
    if i[0] == "L":
        suml+=num
    elif i[0]=="R":
        sumr+=num
    elif i[0]=="U":
        sumu+=num
    else:
        sumd+=num

lr=max(suml,sumr)
ud = max(sumu,sumd)

print(lr,ud)

biggrid = [["." for _ in range(lr*2+1)] for _ in range(ud*2+1)]

#start at lr,ud

for i in inp:
    num = int(i.split(" ")[1])
    for _ in range(num):
        if i[0] == "L":
            lr-=1
        elif i[0]=="R":
            lr+=1
        elif i[0]=="U":
            ud-=1
        else:
            ud+=1
        biggrid[ud][lr]="#"

lr=max(suml,sumr)
ud = max(sumu,sumd)
lr+=1
ud+=1

#floodfill
def floodfill(y,x,step,find,set):
    if y<0 or x<0 or y>=len(biggrid) or x>=len(biggrid[0]):
        return
    if biggrid[y][x]==find:
        biggrid[y][x]=set
        floodfill(y+step,x,step,find,set)
        floodfill(y,x+step,step,find,set)
        floodfill(y-step,x,step,find,set)
        floodfill(y,x-step,step,find,set)

floodfill(ud,lr,1,".","#")

ngrid = [[x for x in l] for l in biggrid]
def counthash(y,line):
    sum=0
    tempsum=0
    toggle=0
    for i,s in enumerate(line):
        if s=="#":
            print("here")
            if (line[i-1]=="." or i==0):
                #toggle=(toggle+1)%2
                ngrid[y][i]=str(toggle)
                sum+=tempsum
            sum+=1
        if s==".":
            if line[i-1]=="#" and i>0:
                toggle+=1
                toggle%=2
            tempsum+=toggle
        if toggle==1:
            ngrid[y][i]="X"
    return sum

s=0
#for y,l in enumerate(biggrid):
#    if not "#" in l:
#        continue
#    s+=counthash(y,l)
    #break
for l in biggrid:
    for x in l:
        if x == "#":
            s+=1
    #print("".join(l))
print(s)


#part2

lr=0
ud =0
points=[]
for l in inp:
    hex = l[:-1].split("#")[1]
    dir = "RDLU"[int(hex[-1])]
    mult = dirs[dir]
    num = int(hex[:-1],16)
    lr+=mult[0]*num
    ud+=mult[1]*num
    print(dir,num)
    points.append((lr,ud))

print(len(inp),len(points),"--")

#points=[(1,6),(3,1),(7,2),(4,4),(8,5)]

def shoelace_section(p,p2):
    print(p,p2, p[0]*p2[1],p[1]*p2[0])
    return p[0]*p2[1]-p[1]*p2[0]

def shoelace():
    s=0
    for i in range(0,len(points)):
        print(points[i])
        s+=shoelace_section(points[i-1],points[i])
    return s/2

print(shoelace())
    
