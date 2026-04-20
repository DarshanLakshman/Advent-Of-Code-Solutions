

vals = []
with open("inputs/day9.txt") as f:
    vals = [x.replace('\n','') for x in f.readlines()]

coords = [tuple(int(x) for x in y.split(',')) for y in vals]
print(coords)
areas = []

for i in range(len(coords)):
    for j in range(i):
        x,y = coords[i]
        a,b = coords[j]
        area = (abs(x-a)+1) * (abs(y-b)+1)
        areas.append(area)

print(max(areas))