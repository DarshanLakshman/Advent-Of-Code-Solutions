
vals = []
with open("inputs/day3.txt") as f:
    vals = [x.strip() for x in f.readlines()]

joltage_sum = 0
for bank in vals:
    first = max(bank[:-1])
    second = max(bank[bank.index(first)+1:])
    print(first, second)
    joltage_sum += int(first) * 10 + int(second)

print(joltage_sum)
