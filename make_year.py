import shutil
import sys
import pathlib
import os
year = sys.argv[1]
try:
    os.mkdir(year)
except:
    pass
to_create = ['part1.py', 'part2.py', 'input.txt', 'test.txt']
for i in range(1, 26):
    try:
        os.mkdir(f'{year}/day_{i:0>2}')
    except:
        pass
    for file in to_create:
        pathlib.Path(f'{year}/day_{i:0>2}/{file}').touch()
