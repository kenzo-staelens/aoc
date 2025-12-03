total_joltage = 0

def get_n_bank_joltage(bank, battery_count):
    bank_joltage = 0
    max_idx = -1
    for position in range(battery_count-1,-1,-1):
        max_joltage = 0
        bank_iter = bank[max_idx+1: -position]
        if position == 0:
            bank_iter = bank[max_idx+1:]
        for i, battery in enumerate(bank_iter, start=max_idx+1):
            if int(battery) > max_joltage:
                max_joltage = int(battery)
                max_idx = i
        bank_joltage = 10*bank_joltage+max_joltage
    return bank_joltage


total_joltage = sum(get_n_bank_joltage(bank, 12) for bank in read())
print(total_joltage)
