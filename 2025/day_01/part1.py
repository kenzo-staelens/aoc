dial = 50
count = 0
for line in read():
    if not line:
        continue # stip blank line
    val = line.replace('L', '-').replace('R', '')
    dial = eval(f"({dial} + {val})%100")
    if dial == 0:
         count += 1

print(count)
