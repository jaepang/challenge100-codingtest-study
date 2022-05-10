import sys
input = sys.stdin.readline

def knapsack(wt, val, n, k):
    memo = [[0] * (k+1) for _ in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(k+1):
            if i == 0 or w == 0:
                memo[i][w] = 0
            elif wt[i] <= w:
                memo[i][w] = max(memo[i-1][w], val[i] + memo[i-1][w-wt[i]])
            else:
                memo[i][w] = memo[i-1][w]
    return memo[n][k]

n, k = map(int, input().split())
weights = [0]
values = [0]
for i in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

print(knapsack(weights, values, n, k))