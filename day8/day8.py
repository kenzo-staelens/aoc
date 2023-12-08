#thanks reddit visualization
#for pointing out that each a/z pair is a cycle
#instead of 1 big mess of connections
from math import gcd

with open ("input.txt","r") as f:
    L = f.read().strip().replace("(","").replace(")","").split('\n')
inst = L[0]
paths = {}
for l in L[2:]:
    start,to = l.split(' = ')
    l,r=to.split(", ")
    paths[(start,"L")]=l
    paths[(start,"R")]=r

mod=len(inst)
def solve(find):
    sum=0
    curr = find
    while True:
        curr = paths[(curr,inst[sum%mod])]
        sum+=1
        if curr[2]==("Z"):
            return sum
print(solve("AAA"))

#part2 solve all cycles
start = [k[0] for k in paths.keys() if k[0][2] == 'A']
print(start)
solves = [solve(k) for k in start]
print(solves)

# calculate least common multiple
lcm = 1
for x in solves:
    lcm*=(x//gcd(lcm,x))
print(lcm)
