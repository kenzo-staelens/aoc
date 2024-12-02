def thecondition(a, b, asc=True):
    if asc:
        return a<b and b-a <= 3 # due to a<b => b-a inherently minimum 1
    return b<a and a-b <= 3 # same logic in reverse


def parseline(line):
    l = [int(x) for x in line.split()]
    lasc = [thecondition(l[x], l[x+1]) for x in range(len(l)-1)]
    ldesc = [thecondition(l[x], l[x+1], False) for x in range(len(l)-1)]
    # print(l, lasc, ldesc)
    return all(lasc) or all(ldesc)


c = 0
with open("input.txt", 'r') as f:
    for line in f.readlines():
        if parseline(line):
            c+=1


print(c)
