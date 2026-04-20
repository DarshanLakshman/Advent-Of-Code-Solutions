
vals = []
with open("inputs/day5.txt") as f:
    vals = [x.strip() for x in f.readlines()]

split_idx = vals.index('')
ranges = [[int(x) for x in rng.split('-')] for rng in vals[:split_idx]]

ranges.sort(key = lambda x: x[1]-x[0], reverse=True)

def new_range(a,b,x,y):
    if x <= a <= y  and x <= b <= y:
        return (x,y)
    if  x <= a <= y and b >= y:
        return (x,b)
    if a < x and x <= b <= y:
        return (a,y)
    if a < x and b > y: 
        return (a,b)
    return (0,0)

def concat_ranges(ranges):
    full_ranges = [ranges[0]]
    for a,b in ranges[1:]:
        range_appended = False

        for i in range(len(full_ranges)): 
            x,y = full_ranges[i]
            new_rng = new_range(a,b,x,y)
            if new_rng != (0,0):
                full_ranges[i] = new_rng
                range_appended = True
                break

        if not range_appended:
            full_ranges.append((a,b))
    return full_ranges
        
changing = True
old,new = concat_ranges(ranges), []
while changing: 
    new = concat_ranges(old)
    if old == new: 
        changing = False
    old = new

print(sum([b-a+1 for a,b in old]))