with open("input.txt","r") as f:
    input = f.read().strip().split(",")

boxes = [[] for _ in range(256)]

def hash(inp):
    temp=0
    for c in inp:
        temp=((temp+ord(c))*17)%256
    return temp

def part2(inp):
    op_idx = max(inp.index("-") if "-" in inp else 0,inp.index("=") if "=" in inp else 0)
    op = inp[op_idx]
    label = inp[:op_idx]
    box = hash(inp[:op_idx])
    
    if op=="=":
        add=True
        for i,item in enumerate(boxes[box]):
            if item.startswith(label):
                boxes[box][i]=inp#overwrite
                add=False
                break
        if add:
            boxes[box].append(inp)
    if op=="-":
        for i,item in enumerate(boxes[box]):
            if item.startswith(label):
                boxes[box].pop(i)

sum = 0
for i in input:
    h = hash(i)
    sum+=h
print("part1:",sum)

for i in input:
    part2(i)

sum=0
for i,box in enumerate(boxes):
    for j,lens in enumerate(box):
        focal = int(lens.split("=")[1])
        sum+=(i+1)*(j+1)*focal
print("part2:",sum)