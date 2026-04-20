from tqdm import tqdm

vals = []
with open("inputs/day7.txt") as f:
    vals = [x.replace('\n','') for x in f.readlines()]

def index_of_all(string, char):
    indexes = []
    for i in range(len(string)):
        if string[i] == char: 
            indexes.append(i)
    return indexes

print(vals)

split_ct = 0
beam_idxs = set([vals[0].index('S')])

for i in tqdm(range(len(vals)-1)): 
    add_beam_idxs = set()
    sub_beam_idxs = set()
    for j in beam_idxs:
        if vals[i+1][j] == '^':
            split_ct += 1
            add_beam_idxs.add(j-1)
            add_beam_idxs.add(j+1)
            sub_beam_idxs.add(j)
            print()
    
    beam_idxs = beam_idxs.union(add_beam_idxs) - sub_beam_idxs
    print(beam_idxs)

print(split_ct)