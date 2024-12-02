#when part 2 gives you *less work* what?
with open("input.txt","r") as f:
    input = f.read().strip().split("\n")

grid = [list(i) for i in input]

expand_p1 = 2 #might as well solve part 1 in the same file
expand_p2 = 1_000_000

def solve(grid, expand):
    galaxies = []
    vinc = 0
    for y,r in enumerate(grid):
        hinc = 0
        if all(i=="." for i in r):
            vinc+=(expand-1)
            continue#nothing here
        for x,s in enumerate(r):
            if all(grid[i][x]=="." for i in range(len(grid))):
                hinc+=(expand-1)
                continue #nothing here
            if s=="#":
                galaxies.append((y+vinc,x+hinc))

    sum = 0
    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            g1,g2 = galaxies[i],galaxies[j]
            sum += abs(g1[0]-g2[0])+abs(g1[1]-g2[1])
    return sum

print("part1: ",solve(grid,expand_p1))
print("part2: ",solve(grid,expand_p2))