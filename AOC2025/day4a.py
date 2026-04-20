
vals = []
with open("inputs/day4.txt") as f:
    vals = [list(x.strip()) for x in f.readlines()]

dirs = [(0,1), (1,0), (0,-1), (-1,0), (-1,-1), (1,1), (1,-1), (-1,1)]

count = 0
for i in range(len(vals)):
    for j in range(len(vals[0])):
        neighbours = [(i+di,j+dj) for di,dj in dirs
                       if 0<=i+di<len(vals) and 0<=j+dj<len(vals[0])]
        neighbour_vals = [vals[x][y] for x,y in neighbours]
        print(neighbours, neighbour_vals)
        if vals[i][j] == "@" and neighbour_vals.count('@') < 4:
            count += 1

print('\n'.join(''.join(x) for x in vals))
print(count)