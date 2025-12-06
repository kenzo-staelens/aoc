import math

print()

arr = []

for line in read():
    if line.strip() == '':
        continue
    # can't strip because whitespace but remove the \n
    arr.append(list(line[:-1]))

ops = {
    '+': sum,
    '*': math.prod
}

results = []
col_vals = []
last_op = None
for c in range(len(arr[0])):
    this_col = [arr[r][c] for r in range(len(arr)-1)]
    if not last_op and arr[-1][c] != ' ':
        last_op = arr[-1][c]
    if all(x == ' ' for x in this_col):
        results.append(ops[last_op](col_vals))
        col_vals = []
        last_op = None
        continue
    # cursed type conversion
    col_val = int(''.join(this_col).replace(' ', ''))
    col_vals.append(col_val)
results.append(ops[last_op](col_vals))
print(sum(results))
