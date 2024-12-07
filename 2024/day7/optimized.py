import itertools
from pprint import pprint

data = []

with open("input.txt","r") as f:
    for line in f.readlines():
        data.append(line.strip().split(": "))

for line in data:
    line[0] = int(line[0])
    line[1] = line[1].split()

def process_list(expect, inp,part):
    if part==1:
        choices=['+','*']
    if part==2:
        choices=['+','*','']
    for opts in itertools.product(choices, repeat=len(inp)-1):
        res = inp[0]
        for item,op in zip(inp[1:],opts):
            res = eval(f"{res}{op}{item}")
        if res==expect:
            return True
    return False

part1 = 0
false_list = []
for i, line in enumerate(data, start=1):
    if i%50 == 0:
        print(i)
    if process_list(*line,1):
        part1+=line[0]
    else:
        false_list.append(line) # realistically must only check these

part2 = part1
print(f"{len(false_list)=}")
for i, line in enumerate(false_list):
    if i%10 == 0:
        print(i)
    if process_list(*line,2):
        part2+=line[0]
print(f'{part1=}\n{part2=}')
