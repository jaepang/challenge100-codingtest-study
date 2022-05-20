# 1410 ~ 1442
'''
3 4 8
....
.T..
....
'''
import sys
input = sys.stdin.readline

def DFS(map, visited, depth, K, cur):
    global R, C
    if depth == K:
        return 1 if cur == (0, C-1) else 0
    elif cur == (0, len(map[0])-1):
        return 0
    
    visited.add(cur)
    ret = 0
    r, c = cur
    if r > 0 and map[r-1][c] != 'T' and (r-1, c) not in visited:
        ret += DFS(map, visited.copy(), depth+1, K, (r-1, c))
    if c > 0 and map[r][c-1] != 'T' and (r, c-1) not in visited:
        ret += DFS(map, visited.copy(), depth+1, K, (r, c-1))
    if r < R-1 and map[r+1][c] != 'T' and (r+1, c) not in visited:
        ret += DFS(map, visited.copy(), depth+1, K, (r+1, c))
    if c < C-1 and map[r][c+1] != 'T' and (r, c+1) not in visited:
        ret += DFS(map, visited.copy(), depth+1, K, (r, c+1))

    
    return ret

R, C, K = map(int, input().split())
map = []
for _ in range(R):
    map.append(input().strip())

print(DFS(map, set(), 1, K, (R-1, 0)))