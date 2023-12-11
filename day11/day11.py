with open("input.txt","r") as f:
    input = f.read().strip().split("\n")

L = [list(i) for i in input]

def expand(g):
    grid = []
    for r in g:
        temp = (r,r) if all(i=="." for i in r) else (r,)
        for nr in temp:
            grid.append(nr)
    return grid
def transpose(g):
    return [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]

def printgrid():
    for r in grid:
        print("".join(r))
    print()

grid = transpose(expand(transpose(expand(L))))

galaxies = []
for y,r in enumerate(grid):
    for x,s in enumerate(r):
        if s=="#":
            galaxies.append((y,x))

print(len(galaxies))

sum = 0
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        g1,g2 = galaxies[i],galaxies[j]
        sum += abs(g1[0]-g2[0])+abs(g1[1]-g2[1])
print(sum)