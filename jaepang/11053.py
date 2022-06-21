import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
ans = 0

for i in range(N):
    cur = 0
    for j in range(i):
        if arr[i] > arr[j]:
            cur = max(cur, dp[j])
    
    dp[i] = cur + 1
    ans = max(ans, dp[i])

print(ans)