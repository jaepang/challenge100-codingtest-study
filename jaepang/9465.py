import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split()))]
    sticker.append(list(map(int, input().split())))
    dp = [[sticker[0][0], sticker[1][0], 0]]
    for i in range(1, N):
        dp.append([])
        dp[i].append(max(dp[i-1][1], dp[i-1][2]) + sticker[0][i])
        dp[i].append(max(dp[i-1][0], dp[i-1][2]) + sticker[1][i])
        dp[i].append(max(dp[i-1][0], dp[i-1][1]))
    print(max(dp[N-1]))