

def blink(n):
    if n == 0:
        return [1]
    if len(str(n)) % 2 == 0:
        return [int(str(n)[:len(str(n))//2]), int(str(n)[len(str(n))//2:])]
    else:
        return [n*2024]
    
def num_stones(stones, blinks):
    for _ in range(blinks):
        print(_)
        new_stones = []
        for s in stones:
            new_stones.extend(blink(s))
        stones = new_stones
    return len(stones)

    
data = """28591 78 0 3159881 4254 524155 598 1"""
stones = [int(x) for x in data.split()]

print(num_stones(stones, 25))

total = 0

for s in stones:
    print(s)
    total += num_stones([s],75)
print(total)

