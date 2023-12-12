# stolen from https://topaz.github.io/paste/#XQAAAQDbBAAAAAAAAAA2GkofDKPu58xTyj67vWUPl6CADq35BUEbaUN3rczsMbz1HfafQMOVDEXzPYXmGqzygAMuI8XVCKliHeen1WSXhr+Yk6uOHWkZViB4xgdw/dIthG5mUiqO7nPoJ39fXFG6Ih7Tx0W9JzjXIMDYWFKa6JK0VSWzHZ3OiYa9i1QlDbOEattWWn6K+5ovRFuTvnhaU5bRomsse+aWq+sjNVkP5oYJzNuJ3FZKLOQEbzlUU1IPO2EBlZ6aLXkKvZI+xtDysT1SrE+lZ14RW/zxdWmIygXatTZJi+AquIS94Hi+nkMd+NgR0yCRGr02P23xi85sFQ/WCcTHHvW2oy91qUeKPKf/DsTGYn8lyMgOcNuulJA2fPaP6PwIjZAk5bR9/06amI9+gl3V9a3kiIbJ8aJ7gVF2llDu0JQnmE6gVIeU0WXQ9aL2orMIKqdfOGyaDrPT7+4mLmo2XTl/Z3hMpIOBrKywPfXVVK+UiKwvOr2g3PgblLXmxX7qotcSIb6Vf0FxSpoxwMtZGKIi8cxWKK8z7dOjrDubZ9YCu1Lgi4dKeb9i7N6AN64TrLbv6L55/LjNsH++L0lwVvfJccDJXKIGyyVsO4BWOcBVBm/KMerXM8971A/8nD9JCQ2DyR2xkA81DulGUZtTU7BOcy3b5f6O/vw=
# idk how to efficiently do this (brute force worked but is deleted)

#understanding of functioning: consume characters untill all accounted for
import re
import functools
with open("input.txt","r") as f:
    input = f.read().strip().split("\n")

#part 1 and 2
@functools.lru_cache #optimization
def f(nums, string):
     if len(nums) == 0:
        #no nums: permute empty space???
        return 1 * '#' not in string
     elif len(string) == 0 or ('?' not in string and '#' not in string):
        #empty string or all . with not empty nums: invalid
        return 0
     else:
        #neither empty
        # [any .] [ fixed num broken/unknown] not followed by #
        first_candidate = re.match(f"^\.*[?#]{{{nums[0]}}}(?!#)", string)
        # [any .] [at least 1 #] or [ any .] [any ?]
        prefix = re.match("^\.*#+|^\.*\?", string)
        if first_candidate is None: 
            if re.match("^\.*#", string):
                return 0
            return f(nums, string[len(prefix[0]):])
        
        first_candidate = first_candidate[0]
        
        # use first candidate
        res = f(nums[1:], string[len(first_candidate)+1:])
        
        # dont use first candidate
        res2 = 0
        if not re.match("^\.*#", string):
            res2 = f(nums, string[len(prefix[0]):])
        return res + res2

def solve(repeat, lines):
    sum = 0
    for i, line in enumerate(lines):
        l = line.strip()
        string, nums = l.split()
        nums = [int(x) for x in re.findall("\d+", nums)]
        
        nums *= repeat
        string = ((string + '?')*repeat)[:-1]
        
        sum += f(tuple(nums), string)
    return sum

print(solve(1,input))
print(solve(5,input))