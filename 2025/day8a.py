
vals = []
with open("inputs/day8.txt") as f:
    vals = [x.replace('\n','') for x in f.readlines()]

coords = [tuple(int(x) for x in y.split(',')) for y in vals]

coord_pair_dists = []

for i in range(len(coords)):
    for j in range(i-1):
        a,b,c = coords[i]
        x,y,z = coords[j]
        dist = (x-a)**2 + (y-b)**2 + (z-c)**2

        coord_pair_dists.append((coords[i],coords[j],dist))

coord_pair_dists.sort(key = lambda x: x[-1])

def coord_circ_index(circuits, coord):
    for i in range(len(circuits)):
        if coord in circuits[i]:
            return i
    return -1

circuits = [[x] for x in coords]

for a,b,dist in coord_pair_dists[:1000]:
    i = coord_circ_index(circuits, a)
    j = coord_circ_index(circuits, b)
    if i != j: 
        circuits[i] += circuits[j]
        circuits.pop(j)

    #print(circuits, i,j, a, b)
    #input()

circ_lengths = (sorted([len(x) for x in circuits]))
print(circ_lengths[-1]*circ_lengths[-2]*circ_lengths[-3])
    



