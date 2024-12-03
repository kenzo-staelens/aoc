import re

with open("input.txt", "r") as f:
    inp = f.read().strip()


rexpr = r"mul\((\d+),(\d+)\)"
res = re.findall(rexpr, inp)
s = sum([int(x[0])*int(x[1]) for x in res])
print(s)
