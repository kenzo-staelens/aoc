import re
from pprint import pprint

with open("input.txt",'r') as f:
    input = f.read()

cards = input.split("\n")

cache = {}

class Card:
    def __init__(self, string):
        idpre,c = string.split(": ")
        self.id = int(re.findall(r'[0-9]+',idpre)[0])
        c = re.sub(r"^ ","",c)
        c = re.sub(r"( +)","  ",c)#fix spaces
        self.w,self.n = c.split("  |  ")
        self.n = f" {self.n} "
        self.wregex = " ("+self.w.replace('  ','|')+") "
    
    def __repr__(self):
        return f"{self.id},{self.w}|{self.n}, {self.wregex}"
    
    def part1(self):
        c = len(self.wins())
        return (1<<(c))>>1
    
    def wins(self):
        return re.findall(self.wregex, self.n)
    
    def part2_cards(self):
        c = len(self.wins())
        return list(range(self.id+1, self.id+c+1))

part1_sum = 0
for card in cards:
    c = Card(card)
    part1_sum += c.part1()
    cache[c.id] = (c.part2_cards(),1)

def processCache2():
    keys = cache.keys()
    sum=0
    for key in keys:
        content,count = cache[key]
        for item in content:
            item_content = cache[item]
            cache[item] = (item_content[0],item_content[1]+count)
        sum+=count
    return sum

print("part1: ", part1_sum, "\npart2: ", processCache2())