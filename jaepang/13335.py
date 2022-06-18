# 2350
import sys
from collections import deque
input = sys.stdin.readline

N, W, L = list(map(int, input().split()))
trucks = deque(map(int, input().split()))
bridge = deque([[1, trucks[0]]])
curWeight = trucks[0]
trucks.popleft()
front = 0
seq = 1
while trucks or bridge:
    for b in bridge:
        b[0] += 1
    if bridge[0][0] > W:
        curWeight -= bridge[0][1]
        bridge.popleft()
    if bridge and trucks:
        if bridge[-1][0] > 1 and curWeight + trucks[0] <= L:
            bridge.append([1, trucks.popleft()])
            curWeight += bridge[-1][1]
    elif trucks:
        bridge.append([1, trucks.popleft()])
        curWeight += bridge[-1][1]

    seq += 1

print(seq)
