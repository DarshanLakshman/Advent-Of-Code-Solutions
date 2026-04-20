
vals = []
with open("inputs/day3.txt") as f:
    vals = [x.strip() for x in f.readlines()]

def next_max(bank, curr_max):
    bank_copy = bank.replace(curr_max, ' ')
    return bank_copy.index(max(bank_copy)), max(bank_copy), bank_copy
    
    


joltage_sum = 0
for val in vals:
    bank = val
    battery = ''

    while len(battery) < 12:
        max_val = max(bank)
        max_val_idx = bank.index(max_val)
        adjusted_bank = bank
        while True:
            if (len(bank) - max_val_idx) >=  12 - len(battery):
                battery += max_val
                bank = bank[max_val_idx+1:]
                break
            else:
                max_val_idx, max_val, adjusted_bank = next_max(adjusted_bank, max_val)
        print(battery)

    joltage_sum += int(battery)

print(joltage_sum)
