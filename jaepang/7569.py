import sys
input = sys.stdin.readline

columns, rows, height = map(int, input().split())
next_matured = []
matured = []
unmatured = set() 
time = 0

for floor in range(height):
    plane = []
    for row in range(rows):
        plane.append(list(map(int, input().split())))
        for col in range(columns):
            if plane[row][col] == 0:
                unmatured.add((floor, row, col))
            elif plane[row][col] == 1:
                next_matured.append((floor, row, col))

while(unmatured):
    time += 1
    matured = next_matured
    next_matured = []
    prev_unmatured_len = len(unmatured)
    for floor, row, col in matured:
        targets = []
        if 0 < floor:
            targets.append((floor-1, row, col))
        if floor < height-1:
            targets.append((floor+1, row, col))
        if 0 < row:
            targets.append((floor, row-1, col))
        if row < rows-1:
            targets.append((floor, row+1, col))
        if 0 < col:
            targets.append((floor, row, col-1))
        if col < columns-1:
            targets.append((floor, row, col+1))

        for target in targets:
            if target in unmatured:
                unmatured.remove(target)
                next_matured.append(target)
    
    if prev_unmatured_len == len(unmatured):
        time = -1
        break

print(time)