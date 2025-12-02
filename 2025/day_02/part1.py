line = next(read())
import math
def find_pattern(min_val, max_val):
    # pad even
    # length difference between min and max is at most 1

    # comment after the fact
    # ranges are *much smaller* than i expected them to be :/
    # oh well, at least this is lightning fast
    if len(min_val) % 2 == len(max_val) % 2 == 1:
        return (0, 0) # both would have leading zero
    if len(min_val) % 2 == 1:
        min_val = '0'+min_val
    if len(max_val) % 2 == 1:
        max_val = '0' + max_val
    cut_len = len(min_val) // 2
    # inner section
    mv = int(min_val[:-cut_len])
    mav = int(max_val[:-cut_len])
    tail_mv = int(min_val[-cut_len:])
    tail_mav = int(max_val[-cut_len:])
    dups = 0
    for i in range(mv+1, mav):
        if len(str(i)) != cut_len:
            continue
        dups += i*(10**cut_len + 1)

    if mv < mav and mv >= tail_mv and len(str(mv)) == cut_len:
        dups += mv*(10**cut_len + 1)
    if mv < mav and mav <= tail_mav and len(str(mav)) == cut_len:
        dups += mav*(10**cut_len + 1)
    if mv == mav and tail_mv <= mv <= tail_mav:
        dups += mv*(10**cut_len + 1)
    return dups, cut_len
i=0
d = 0

for item in line.split(','):
    a,b = item.split('-')
    dups = find_pattern(a,b)
    d+= dups[0]
print(d)
