from tqdm import tqdm
systems=[]

for x in inp.split("\n\n"):
    s = x.split("\n")
    e1=[int(a[2:]) for a in s[0][10:].split(", ")]
    e2=[int(a[2:]) for a in s[1][10:].split(", ")]
    o = [1*10_000_000_000_000+int(a[2:]) for a in s[2][7:].split(", ")]
    systems.append([e1,e2,o])
import numpy as np

sc = 0

for system in tqdm(systems):
    R = [[system[0][0],system[1][0]],
         [system[0][1],system[1][1]]]
    A,B = np.linalg.solve(R,system[2])
    if all(round(A)*system[0][i]+round(B)*system[1][i]==system[2][i] for i in range(2)):
        sc+= round(A)*3+round(B)
print(sc)
