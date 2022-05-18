import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, vertex, k):
    queue = deque()
    visited = set([vertex])
    for v in graph[vertex]:
        queue.append((v, graph[vertex][v]))
    recommends = set()

    while queue:
        cur, usado = queue.popleft()
        if usado >= k:
            recommends.add(cur) 

            for v in graph[cur]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, min(usado, graph[cur][v])))
        elif cur in recommends:
            recommends.remove(cur)

    return len(recommends)

N, Q = map(int, input().split())
graph = {}
for i in range(N-1):
    v1, v2, e = map(int, input().split())
    if v1 not in graph:
        graph[v1] = dict()
    graph[v1][v2] = e
    if v2 not in graph:
        graph[v2] = dict()
    graph[v2][v1] = e

for j in range(Q):
    k, v = map(int, input().split())
    print(BFS(graph, v, k))
