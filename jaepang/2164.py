from collections import deque
N = int(input())

queue = deque(range(1, N+1))
round = 1
while len(queue) > 1:
    front = queue.popleft()
    if round % 2 == 0:
        queue.append(front)
    round = (round + 1) % 2

print(queue[0])
