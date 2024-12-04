import re


option1 = [['M', 'M'], ['S', 'S']]
option2 = [['S', 'S'], ['M', 'M']]
option3 = [['M', 'S'], ['M', 'S']]
option4 = [['S', 'M'], ['S', 'M']]

options=[option1, option2, option3, option4]

with open('input.txt', 'r') as f:
    inp = f.read().strip().split("\n")


count = 0
tag=False
for y in range(len(inp)-2):
    for x in range(len(inp[0])-2):
        p5 = inp[y+1][x+1]=='A'
        for option in options:
            p1 = inp[y][x]==option[0][0]
            p2 = inp[y+2][x]==option[1][0]
            p3 = inp[y][x+2]==option[0][1]
            p4 = inp[y+2][x+2]==option[1][1]
            if p1 and p2 and p3 and p4 and p5:
                count+=1
                break


print(count)
