import itertools
from pprint import pprint

antennas = dict()

numantennas = 0
nodes = set()


with open("input.txt",'r') as f:
	for y, line in enumerate(f.readlines()):
		for x, char in enumerate(line.strip()):
			if char !='.':
				if char not in antennas:
					antennas[char] = set()
				antennas[char].add((x,y))
				nodes.add((x,y))
max_x = x
max_y = y



for _, v in antennas.items():
	combos = list(itertools.combinations(v,2))
	for p1, p2 in combos:
		dx = p2[0]-p1[0]
		dy = p2[1]-p1[1]
		
		while 0 <= p1[0]-dx <= max_x and 0 <= p1[1]-dy <=max_y:
			nodes.add((p1[0]-dx, p1[1]-dy))
			p1 = (p1[0] - dx, p1[1] - dy)
		while 0 <= p2[0]+dx <= max_x and 0 <= p2[1]+dy <=max_y:
			nodes.add((p2[0]+dx, p2[1]+dy))
			p2 = (p2[0] + dx, p2[1] + dy)

print(len(nodes))