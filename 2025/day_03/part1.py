total_joltage = 0
for bank in read():
    bank_joltage = 0
    max_joltage, max_idx = 0, -1
    for i, battery in enumerate(bank[:-1]):
        if int(battery) > max_joltage:
            max_joltage = int(battery)
            max_idx = i
    bank_joltage = 10*max_joltage
    max_joltage = 0
    for battery in bank[max_idx+1:]:
        if int(battery) > max_joltage:
            max_joltage = int(battery)
    total_joltage += bank_joltage + max_joltage
print(total_joltage)
