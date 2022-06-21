import sys
input = sys.stdin.readline

N = int(input())
cost = []
for i in range(N):
    cost.append(list(map(int, input().split())))
    if i == 0:
        dp = [cost[0]]
    else:
        dp.append([])
        dp[i].append(min(dp[i-1][1], dp[i-1][2]) + cost[-1][0])
        dp[i].append(min(dp[i-1][0], dp[i-1][2]) + cost[-1][1])
        dp[i].append(min(dp[i-1][0], dp[i-1][1]) + cost[-1][2])

print(min(dp[N-1]))