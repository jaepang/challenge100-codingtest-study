# 1605 ~ 1635
import sys
input = sys.stdin.readline

N, goal = list(map(int, input().split()))
coins = []
dp = [1] + [0] * goal
for _ in range(N):
    coins.append(int(input()))

for coin in coins:
    for i in range(coin, goal+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[goal])

'''
3 10
1
2
5

1 * 10
1 * 8 + 2 * 1
1 * 6 + 2 * 2
1 * 4 + 2 * 3
1 * 2 + 2 * 4
2 * 5

1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 1 1 1
1 2 2 3 3 4 4 5 5 6
1 2 2 3 4 5 6 6 8 10

'''