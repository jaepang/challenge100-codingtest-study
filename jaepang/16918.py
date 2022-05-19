import sys
import re
input = sys.stdin.readline

R, C, N = map(int, input().split())
map = []
bombs = {}
for r in range(R):
    row = input().strip()
    map.append(list(row))

for t in range(1, N+1):
    if t == 1:
        bombs[t-1] = []
        for r, row in enumerate(map):
            bombs[t-1] += [(r, m.start()) for m in re.finditer('O', ''.join(row))]
    elif t % 2 == 0:
        for i in range(R):
            for j in range(C):
                map[i][j] = 'O'
    else:
        for r, c in bombs[t-3]:
            map[r][c] = '.'
            if 0 < r:
                map[r-1][c] = '.'
            if r < R-1:
                map[r+1][c] = '.'
            if 0 < c:
                map[r][c-1] = '.'
            if c < C-1:
                map[r][c+1] = '.'

        bombs[t-1] = []
        for r, row in enumerate(map):
            bombs[t-1] += [(r, m.start()) for m in re.finditer('O', ''.join(row))]

for row in map:
    print(''.join(row))
