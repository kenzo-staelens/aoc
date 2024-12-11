import functools
import collections

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
for i  in range(75):
    for stone, c in stones.items():
        res = apply_rule(stone)
        for s in res:
            newstones[s] = newstones.get(s,0)+c
    stones = newstones
    newstones = {}
    if i==24:
        pt1 = sum(stones.values())
pt2 = sum(stones.values())
print(f"{pt1=}")
print(f"{pt2=}")
