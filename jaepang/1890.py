# 2104~2121
import sys
input = sys.stdin.readline

N = int(input())
board = []
dp = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    dp.append([0] * N)
dp[0][0] = 1

for r, row in enumerate(board):
    for c, point in enumerate(row):
        if point == 0:
            break
        if r+point < N:
            dp[r+point][c] += dp[r][c]
        if c+point < N:
            dp[r][c+point] += dp[r][c]

print(dp[N-1][N-1])