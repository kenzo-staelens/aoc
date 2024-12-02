import re
with open ("input.txt","r") as f:
    input = f.read().strip().split('\n\n')

def verify_mirror(lines,line,count):
    return all(lines[line-i]==lines[line+i+1] for i in range(count))

def verify_smudged(lines,line,count,expect_diff):
    #print("--",line,count)
    diffs = 0
    for i in range(count):
        if lines[line-i]==lines[line+i+1]:
            #ok
            continue
        for j in range(len(lines[0])):
            diffs+=lines[line-i][j]!=lines[line+i+1][j]
            if diffs>expect_diff:
                #too many diffs
                #print("return for",diffs ,">",expect_diff)
                return False
    return diffs==expect_diff

def parse_input(block,expect_diffs):
    lines = block.split("\n")
    #find where i=i+1
    for i in range(len(lines)-1):
        lc=min(len(lines)-i-1,i+1)
        if lines[i]==lines[i+1]:
            pass
            #if verify_mirror(lines,i,lc):
            #    return i+1
            
        if verify_smudged(lines,i,lc,expect_diffs):
            return i+1
    return 0

def transpose(block):
    lines=block.split("\n")
    newlines=[[] for _ in range(len(lines[0]))]
    for line in lines:
        for j,c in enumerate(line):
            newlines[j].append(c)
    #reconstruct
    return "\n".join(["".join(x) for x in newlines])

def solve(diffs):
    sum=0
    for i in input:
        c = parse_input(i,diffs)*100
        #print(c)
        if c==0:
            i=transpose(i)
            c=parse_input(i,diffs)
            #print(c)
        sum+=c
    return sum

print(solve(0))#part1
print(solve(1))#part2
