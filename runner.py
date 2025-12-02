#!/usr/bin/python3
import argparse
import shutil
import os
import dotenv
from itertools import product
import time

dotenv.load_dotenv('settings')
YEAR = os.environ.get('YEAR')
DAY = os.environ.get('DAY')

parser = argparse.ArgumentParser(prog='AoC')
parser.add_argument('-f', '--file', choices={'input', 'test'}, required=True)
parser.add_argument('-d', '--day', type=int, required=(not DAY), action="append")
parser.add_argument('-p', '--part', type=int, choices={1,2}, required=True, action="append")
args = parser.parse_args()

def get_base_runnable():
    runnable = ''
    with open('tools/reader.py', 'r') as f:
        runnable += f.read()
    return runnable

def with_newlines(values):
    newline = ''
    for value in sorted(values):
        yield newline, value
        newline = '\n'

days = args.day or [DAY]
for nl_day, day in with_newlines(days):
    print(f'{nl_day}Day {day}:')
    daypath = f'{YEAR}/day_{day:0>2}'
    base_runnable = get_base_runnable()
    shutil.copyfile(f'{daypath}/{args.file}.txt' ,'input.txt')
    for nl_part, part in with_newlines(args.part):
        with open(f'{daypath}/part{part}.py', 'r') as f:
            runnable = base_runnable + f.read()
        print(f'{nl_part}  Part: {part}\n    ', end='')
        start = time.time()
        exec(runnable)
        end = time.time()
        print(f'    ran in: {(end-start)*1000}ms')
    os.remove('input.txt')
