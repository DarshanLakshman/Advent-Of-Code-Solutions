range_lst = []
with open("inputs/day2.txt") as f:
    range_lst = f.readline().split(',')

def is_invalid(num):
    for x in range(1,len(num)//2+1):
        if num[:x] * (len(num)//x) == num:
            return True
    return False

invalid_sum = 0
for rng in range_lst:
    a,b = [int(x) for x in rng.split('-')]

    for num in range(a,b+1):
        if is_invalid(str(num)): 
            print(num)
            invalid_sum += num

print(invalid_sum)