

vals = []
with open("inputs/day7.txt") as f:
    vals = [x.replace('\n','') for x in f.readlines()]

def merging(lst):
    val_set = set([x[0] for x in lst])
    new_lst = []
    for x in val_set:
        print(x)
        new_lst.append((x, sum([l[1] for l in lst if l[0] == x])))
    return new_lst

beam_idxs = [(vals[0].index('S'),1)]

for i in (range(len(vals)-1)): 
    print(i, len(beam_idxs))
    add_beam_idxs = []
    sub_beam_idxs = []

    for j,ct in beam_idxs:
        if vals[i+1][j] == '^':
            add_beam_idxs.append((j-1,ct))
            add_beam_idxs.append((j+1,ct))
            sub_beam_idxs.append((j,ct))
        
    add_beam_idxs = merging(add_beam_idxs)
    
    for x in sub_beam_idxs:
        beam_idxs.remove(x)
    
    beam_idxs += add_beam_idxs

print(sum(x[1] for x in beam_idxs))

            
