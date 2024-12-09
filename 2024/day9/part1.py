with open('input.txt','r') as f:
    inp = [int(x) for x in f.read().strip()]
    data = inp[::2]
    holes = inp[1::2]

print(data)
print(holes)

res = []

for i, (dp,hole) in enumerate(zip(data, holes+[0])):
    res+=[i]*dp+[-1]*hole

start = 0
end = len(res)-1

while start<end:
    if res[start]!=-1:
        start+=1
    else:
        while res[end]==-1:
            res[end]=0
            end-=1
        res[start]=res[end]
        res[end] = -1
res[end]=0
print(sum(res[i]*i for i in range(len(res))))
