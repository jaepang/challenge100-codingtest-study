import sys
input = sys.stdin.readline

P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
top = 10

T = int(input())
for _ in range(T):
    n = int(input())
    if n > top:
        for i in range(top+1, n+1):
            P.append(P[i-1] + P[i-5])
        top = n
    print(P[n])