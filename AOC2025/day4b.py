
vals = []
with open("inputs/day4.txt") as f:
    vals = [list(x.strip()) for x in f.readlines()]

dirs = [(0,1), (1,0), (0,-1), (-1,0), (-1,-1), (1,1), (1,-1), (-1,1)]

total_count = 0
count_changing = True

while count_changing: 
    removable_rolls = []
    for i in range(len(vals)):
        for j in range(len(vals[0])):
            neighbours = [(i+di,j+dj) for di,dj in dirs
                        if 0<=i+di<len(vals) and 0<=j+dj<len(vals[0])]
            neighbour_vals = [vals[x][y] for x,y in neighbours]
 
            if vals[i][j] == "@" and neighbour_vals.count('@') < 4:
                removable_rolls.append((i,j))

    if len(removable_rolls) == 0:
        count_changing = False
    else:
        for m,n in removable_rolls:
            vals[m][n] = '.'
        total_count +=  len(removable_rolls)
    print(total_count, removable_rolls)
        

print('\n'.join(''.join(x) for x in vals))
print(total_count)