
vals = []
with open("inputs/test.txt") as f:
    vals = [x.replace('\n','') for x in f.readlines()]

def prod(lst):
    product = 1
    for x in lst:
        product *= x
    return product

col_ct = len(vals)
row_length = len(vals[0])

num_lst = []
total = 0
for i in range(row_length):
    column = [vals[x][row_length - i - 1] for x in range(len(vals))]
    print(column)

    if not all(x==' ' for x in column):
        num_lst.append(int(''.join(column[:-1])))

        if column[-1] == "*":
            total += prod(num_lst)
            num_lst = []
        elif column[-1] == "+":
            total += sum(num_lst)
            num_lst = []

print(total)
    