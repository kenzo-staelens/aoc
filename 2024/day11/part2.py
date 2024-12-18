import functools
import collections
import time
start = time.time()
with open("input.txt","r") as f:
    stones = [int(x) for x in f.read().strip().split()]

stones = collections.Counter(stones)

print(stones)
@functools.cache
def apply_rule(stone):
    if stone==0:
        return [1]
    if len(str(stone))%2==0:
        strstone = str(stone)
        lenstone = len(strstone)
        return [int(strstone[:lenstone//2]), int(strstone[lenstone//2:])]
    return [stone*2024]

newstones = {}
for i  in range(49000):
    if not i%1000:
        print(f"iter {i}")
    for stone, c in stones.items():
        res = apply_rule(stone)
        for s in res:
            newstones[s] = newstones.get(s,0)+c
    stones = newstones
    newstones = {}
    if i==24:
        pt1 = sum(stones.values())
    if i == 24705:
        print(time.time()-start)
print(time.time()-start)
pt2 = sum(stones.values())

print(f"{pt1=}")
print(f"{pt2=}")
