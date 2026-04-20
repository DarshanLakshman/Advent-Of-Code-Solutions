from itertools import combinations

# Read input
vals = []
with open("inputs/day9.txt") as f:
    vals = [x.strip() for x in f.readlines()]

# Parse coordinates
coords = [tuple(int(x) for x in y.split(',')) for y in vals]
line_segments = [coords[i:i+2] for i in range(len(coords)-1)]
line_segments.append([coords[-1], coords[0]])

def intersect(l1, rectangle):
    # Rectangle bounds
    x_min, x_max = sorted([rectangle[0][0], rectangle[2][0]])
    y_min, y_max = sorted([rectangle[0][1], rectangle[2][1]])
    
    (x1, y1), (x2, y2) = l1
    
    # Horizontal line
    if y1 == y2:
        y = y1
        if y_min < y < y_max:
            # Check if x-range overlaps
            line_x_min, line_x_max = sorted([x1, x2])
            if line_x_max > x_min and line_x_min < x_max:
                return True
        return False
    
    # Vertical line
    if x1 == x2:
        x = x1
        if x_min < x < x_max:
            # Check if y-range overlaps
            line_y_min, line_y_max = sorted([y1, y2])
            if line_y_max > y_min and line_y_min < y_max:
                return True
        return False

areas = []      
for i in range(len(coords)):
    for j in range(i):
        x, y = coords[i]
        a, b = coords[j]

        # Rectangle corners (polygon) instead of edges
        rectangle = [(x, y), (a, y), (a, b), (x, b)]

        valid = True

        for l1 in line_segments:
            if intersect(l1, rectangle):
                valid = False
            
        if valid:
            area = (abs(x-a)+1) * (abs(y-b)+1)
            areas.append(area)

print(max(areas))

    

        
