import functools

with open("input.txt","r") as f:
    stones = [int(x) for x in f.read().strip().split()]

@functools.cache
def apply_rule(stone):
    if stone==0:
        return [1]
    if len(str(stone))%2==0:
        strstone = str(stone)
        lenstone = len(strstone)
        return [int(strstone[:lenstone//2]), int(strstone[lenstone//2:])]
    return [stone*2024]

newstones = []
for _ in range(25):
    for stone in stones:
        newstones+=apply_rule(stone)
    stones = newstones[:]
    newstones = []
print(len(stones))
