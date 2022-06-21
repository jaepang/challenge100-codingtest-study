import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
L = []

for num in arr:
    if len(L) == 0 or L[-1] < num:
        L.append(num)
    else:
        L[bisect_left(L, num)] = num

print(len(L))