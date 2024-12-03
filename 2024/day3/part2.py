import re

with open("input.txt", "r") as f:
    inp = f.read().strip()


rexpr = r"mul\(\d+,\d+\)|do(?:n't)?\(\)"
res = re.findall(rexpr, inp) # eh it's <1000 entries
print(res)
def mul(a,b):
    return int(a)*int(b)

s=0
state = True
for entry in res:
    match entry:
        case "don't()":
            state = False
        case "do()":
            state = True
        case _:
            if not state:
                continue
            s+=mul(*re.findall(r"\d+", entry))
print(s)
