# 1838 ~ 1852
import sys
input = sys.stdin.readline

N, goal = list(map(int, input().split()))
coins = []
for _ in range(N):
    coins.append(int(input()))
dp = [0] + [float('inf')] * goal

for coin in coins:
    for i in range(coin, goal+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[goal] == float('inf'):
    print(-1)
else:
    print(dp[goal])
