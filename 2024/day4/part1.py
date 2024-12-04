import re

with open('input.txt', 'r') as f:
    inp = f.read().strip().split("\n")


def find_in_line(lines):
    c = 0
    for line in lines:
        for idx in range(len(line)-3):
            if line[idx:idx+4] in {'XMAS', 'SAMX'}:
                c+=1
    return c


def find_vertical(lines):
    c = 0
    for col in range(len(lines[0])):
        for idx in range(len(lines)-3):
            text = ''.join(lines[idx+x][col] for x in range(4))
            if text in {'XMAS', 'SAMX'}:
                c+=1
    return c


def find_diagonal(lines):
    c = 0
    for y in range(len(lines)-3):
        for x in range(len(lines[0])-3):
            text = ''.join(lines[y+i][x+i] for i in range(4))
            text2 = ''.join(lines[
                                len(lines)-y-i-1
                            ][
                                x+i
                            ] for i in range(4))
            if text in {'XMAS', 'SAMX'}:
                c+=1
            if text2 in {'XMAS', 'SAMX'}:
                c+=1
            print(f"{x=} {y=} {text2=}", text2 in {'XMAS', 'SAMX'})
    return c


count = 0
count+=find_in_line(inp)
print(count)
count+=find_vertical(inp)
print(count)
count+=find_diagonal(inp)
print(count)
