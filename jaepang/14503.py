import sys
input = sys.stdin.readline

def rotate(arr, direction):
    padding = -(direction % 4)
    new_arr = arr[padding:] + arr[:padding]
    return new_arr


def step_back(row, col, direction):
    if direction == 0:
        return (row+1, col)
    elif direction == 1:
        return (row, col-1)
    elif direction == 2:
        return (row-1, col)
    elif direction == 3:
        return (row, col+1)


height, width = map(int, input().split())
cur = tuple(map(int, input().split()))
cleans = 0
room = []
dirty = set()
clean = set()

for r in range(height):
    room.append(list(map(int, input().split())))
    for c in range(width):
        if room[r][c] == 0:
            dirty.add((r, c))

while (dirty):
    row, col, direction = cur
    pos = (row, col)
    if pos in dirty:
        dirty.remove(pos)
        clean.add(pos)
        cleans += 1

    # north west south east
    coordinates = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
    for coor in coordinates:
        available = coor in dirty
        if available:
            break
    targets = rotate(coordinates, direction)

    if not available:
        # try step-back
        r, c = step_back(row, col, direction)
        if room[r][c] == 1:
            break
        cur = (r, c, direction)

    else:
        target = targets[1]
        new_row, new_col = target
        new_direction = (direction-1) % 4
        if (new_row, new_col) in dirty:
            cur = (new_row, new_col, new_direction)
        else:
            cur = (row, col, new_direction)

print(cleans)