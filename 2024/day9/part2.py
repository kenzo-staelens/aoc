data = []
toggle = True
idx = 0
i = 0
with open('input.txt','r') as f:
    inp = [int(x) for x in f.read().strip()]
    for x in inp:
        if toggle:
            data+=[[x, i]]
            i += 1
            toggle= False
            idx+=x
        else:
            data+=[[x,-1]]
            toggle=True
            idx += x

def print_data(d):
    s = ''
    for item in d:
        s += str(item[1])*item[0] if item[1]!=-1 else '.'*item[0]
    print(s)


end = len(data)-1
while end>-1:
    if data[end][1]==-1:
        end-=1
        continue
    for i in range(end):
        if data[i][0]==data[end][0] and data[i][1]==-1:
            data[i][1] = data[end][-1]
            data[end][1] = -1
            break
        if data[i][0]>data[end][0] and data[i][1]==-1:
            data[i][0]-=data[end][0]
            endcopy = [data[end][0],data[end][1]]
            data.insert(i,endcopy)
            data[end+1][1] = -1
            end+=1
            break
    end-=1

res = []
for item in data:
    res += [item[1]]*item[0] if item[1]!=-1 else [0]*item[0]
print(sum(res[i]*i for i in range(len(res))))
