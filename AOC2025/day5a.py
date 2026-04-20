
vals = []
with open("inputs/day5.txt") as f:
    vals = [x.strip() for x in f.readlines()]

split_idx = vals.index('')
ranges = [[int(x) for x in rng.split('-')] for rng in vals[:split_idx]]
ids = [int(x) for x in vals[split_idx+1:]]

fresh_count = 0
for id in ids:
    if any(a<=id<=b for a,b in ranges):
        fresh_count +=1
print(fresh_count)
