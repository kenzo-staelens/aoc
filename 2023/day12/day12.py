# stolen from https://topaz.github.io/paste/#XQAAAQDbBAAAAAAAAAA2GkofDKPu58xTyj67vWUPl6CADq35BUEbaUN3rczsMbz1HfafQMOVDEXzPYXmGqzygAMuI8XVCKliHeen1WSXhr+Yk6uOHWkZViB4xgdw/dIthG5mUiqO7nPoJ39fXFG6Ih7Tx0W9JzjXIMDYWFKa6JK0VSWzHZ3OiYa9i1QlDbOEattWWn6K+5ovRFuTvnhaU5bRomsse+aWq+sjNVkP5oYJzNuJ3FZKLOQEbzlUU1IPO2EBlZ6aLXkKvZI+xtDysT1SrE+lZ14RW/zxdWmIygXatTZJi+AquIS94Hi+nkMd+NgR0yCRGr02P23xi85sFQ/WCcTHHvW2oy91qUeKPKf/DsTGYn8lyMgOcNuulJA2fPaP6PwIjZAk5bR9/06amI9+gl3V9a3kiIbJ8aJ7gVF2llDu0JQnmE6gVIeU0WXQ9aL2orMIKqdfOGyaDrPT7+4mLmo2XTl/Z3hMpIOBrKywPfXVVK+UiKwvOr2g3PgblLXmxX7qotcSIb6Vf0FxSpoxwMtZGKIi8cxWKK8z7dOjrDubZ9YCu1Lgi4dKeb9i7N6AN64TrLbv6L55/LjNsH++L0lwVvfJccDJXKIGyyVsO4BWOcBVBm/KMerXM8971A/8nD9JCQ2DyR2xkA81DulGUZtTU7BOcy3b5f6O/vw=
# idk how to efficiently do this (brute force worked but is deleted)

#understanding of functioning: consume characters until all accounted for
import re
import functools
with open("../input.txt","r") as f:
    input = f.read().strip().split("\n")

#part 1 and 2
@functools.lru_cache #memoization
def f(nums, string):
     if len(nums) == 0:
        #if no nums left: return 1 if # not in string else 0 ?
        # = return 1 if valid solution
        return 1 * '#' not in string
     elif len(string) == 0 or ('?' not in string and '#' not in string):
        #string is empty but there are still numbers -> not a solution
        return 0
     else:
        #neither empty -> continue processing
        # [any .] [ fixed num broken/unknown] not followed by #
        # = contiguous group of isolated (possibly) broken springs
        first_candidate = re.match(f"^\.*[?#]{{{nums[0]}}}(?!#)", string)
        
        # [any .] [at least 1 #] or [ any .] [any ?]
        # group of springs starts with ? or # -> get that character and any preceding .
        prefix = re.match("^\.*#+|^\.*\?", string)
        if first_candidate is None: # if no group found
            if re.match("^\.*#", string): # but a spring does exist
                # num > next group length -> not a solution
                return 0
            #else return recursive stripped prefix (i believe this becomes "")
            return f(nums, string[len(prefix[0]):])
        
        first_candidate = first_candidate[0] # unwrap
        
        # use first candidate
        # recursive processing with first number & group removed
        res = f(nums[1:], string[len(first_candidate)+1:])
        
        # dont use first candidate
        res2 = 0
        if not re.match("^\.*#", string):
            # strip prefix if it was a ? & try processing too
            res2 = f(nums, string[len(prefix[0]):])
        return res + res2 # sum of both branches

def solve(repeat, lines):
    sum = 0
    for i, line in enumerate(lines):
        #for each line
        l = line.strip()
        string, nums = l.split() # parse the line
        nums = [int(x) for x in re.findall("\d+", nums)] # make nums numbers
        
        string = ((string + '?')*repeat)[:-1] # expand the string separate by ?
        nums *= repeat # multiply the numbers array to account for expansion
        
        sum += f(tuple(nums), string) #process the line
    return sum

print(solve(1,input))
print(solve(5,input))