import itertools
from pprint import pprint

data = []

with open("input.txt","r") as f:
    for line in f.readlines():
        data.append(line.strip().split(": "))

for line in data:
    line[0] = int(line[0])
    line[1] = line[1].split()

def process_list(expect, inp):
    for opts in itertools.product(['+','*'], repeat=len(inp)-1):
        res = inp[0]
        for item,op in zip(inp[1:],opts):
            res = eval(f"{res}{op}{item}")
        if res==expect:
            return True
    return False

count = 0
for i, line in enumerate(data, start=1):
    
    if i%50 == 0:
        print(i)
    if process_list(*line):
        count+=line[0]
print(count)