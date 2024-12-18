from tqdm import tqdm
systems=[]

for x in inp.split("\n\n"):
    s = x.split("\n")
    e1=[int(a[2:]) for a in s[0][10:].split(", ")]
    e2=[int(a[2:]) for a in s[1][10:].split(", ")]
    o = [10_000_000_000_000+int(a[2:]) for a in s[2][7:].split(", ")]
    systems.append([e1,e2,o])

sc = 0
for system in tqdm(systems):
    min = 0
    for A in range(1000000000000):
        if any(system[0][i]*A > system[2][i] for i in range(2)):
            break
        for B in range(1000000000000):
            if any(system[0][i]*A + system[1][i]*B > system[2][i] for i in range(2)):
                break
            if all(system[0][i]*A+system[1][i]*B == system[2][i] for i in range(2)):
                if 3*A+B<min or min==0:
                    min = 3*A+B
    sc += min
print(sc)
