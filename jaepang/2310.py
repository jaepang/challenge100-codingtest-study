import sys
input = sys.stdin.readline

def DFS(n, visited, pos, money):
    global category, amount, graph
    if pos == n-1:
        return category[pos] != 'T' or amount[pos] <= money

    visited.add(pos)
    if category[pos] == 'T':
        money -= amount[pos]
        if money < 0:
            return False
    elif category[pos] == 'L':
        money = max(money, amount[pos])

    for room in graph[pos]:
        if room not in visited:
            case = DFS(n, visited.copy(), room, money)
            if case:
                return True

    return False

size = int(input())
while size > 0:
    category = []
    amount = []
    graph = dict()
    for i in range(size):
        info = input().split()
        category.append(info[0])
        amount.append(int(info[1]))
        graph[i] = [i-1 for i in map(int, info[2:-1])]

    print('Yes') if DFS(size, set(), 0, 0) else print('No')
    size = int(input())