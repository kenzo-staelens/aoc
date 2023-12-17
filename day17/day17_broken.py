#works on test case and part 1
import heapq
with open ("test.txt","r") as f:
    inp = f.read().strip().split("\n")

#grid
inp = [[int(x) for x in l] for l in inp]

#> v < ^
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

queue =[]
seen = {}

#heat, row,col,dir,traveled
heapq.heappush(queue,(0,0,0,0,0))
heapq.heappush(queue,(0,0,0,1,0))
H=len(inp[0])
W=len(inp)

bounds=(0,3) #edit here for p2
bounds=(4,10)
while queue:
    h,r,c,d,t = heapq.heappop(queue)
    #print(h,r,c)
    if c<0 or c>W or r<0 or r>H:
        #print(H,W,r,c)
        continue
    if (r,c,d,t) in seen:
        continue
    seen[(r,c,d,t)]=h
    #if r == H-1 and c==W-1:
    #    continue
    
    #push new items
    try:
        dnew = d
        rnew = r+dirs[dnew][0]
        cnew = c+dirs[dnew][1]
        hnew = h+inp[cnew][rnew]
        tnew = t+1
        if t<bounds[1]:
            heapq.heappush(queue,(hnew,rnew,cnew,dnew,tnew))
    except:
        pass
    if t>=bounds[0]:
        for x in [-1,1]:
            try:
                dnew = (d+4+x)%4
                rnew = r+dirs[dnew][0]
                cnew = c+dirs[dnew][1]
                hnew = h+inp[cnew][rnew]
                heapq.heappush(queue,(hnew,rnew,cnew,dnew,1))
            except Exception as e:
                pass

min = 999999
print(W,H)
solve=None
for key,item in seen.items():
    if key[0]==H-1 and key[1]==W-1:
        if item<min:
            solve=item
            min=item
print(solve)
print("r,c,d,t")
for r,c,_,_ in seen.keys():
    pass
    #if r>=12:
        #print(r,c)
input()
