import sys
input = sys.stdin.readline

def DFS(row, col):
    global height, width, mountMap, dp
    if dp[row][col] != -1:
        return dp[row][col]
    cur = mountMap[row][col]
    ret = 0
    if row > 0 and mountMap[row-1][col] < cur:
        ret += DFS(row-1, col) 
    if row < height-1 and mountMap[row+1][col] < cur:
        ret += DFS(row+1, col)
    if col > 0 and mountMap[row][col-1] < cur:
        ret += DFS(row, col-1) 
    if col < width-1 and mountMap[row][col+1] < cur:
        ret += DFS(row, col+1)
    dp[row][col] = ret
    return dp[row][col]

height, width = list(map(int, input().split()))
mountMap = []
dp = []
for _ in range(height):
    mountMap.append(list(map(int, input().split())))
    dp.append([-1] * width)

dp[height-1][width-1] = 1
DFS(0, 0)
print(dp[0][0])
