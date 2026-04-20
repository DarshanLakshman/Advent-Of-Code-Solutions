
vals = []
with open("inputs/day6.txt") as f:
    vals = [x.replace('\n','') for x in f.readlines()]

operators = [x for x in vals[-1].split(' ') if x != '']
nums = [[int(x) for x in row.split(' ') if x != ''] for row in vals[:-1]]

print(operators)

def prod(lst):
    product = 1
    for x in lst:
        product *= x
    return product

total = 0
for i, op in enumerate(operators):
    column = [nums[x][i] for x in range(len(nums))]
    print(column, i)
    if op == "*":
        total += prod(column)
    elif op == '+':
        total += sum(column)

print(total)

