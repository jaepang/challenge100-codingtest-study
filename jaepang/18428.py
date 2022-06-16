# 2226 ~ 2320
import copy

def isSafe(teachers, hallway, size):
    for row, col in teachers:
        for r in reversed(range(row)):
            if hallway[r][col] == 'O':
                break
            elif hallway[r][col] == 'S':
                return False
        for r in range(row, size):
            if hallway[r][col] == 'O':
                break
            elif hallway[r][col] == 'S':
                return False

        for c in reversed(range(col)):
            if hallway[row][c] == 'O':
                break
            elif hallway[row][c] == 'S':
                return False
        for c in range(col, size):
            if hallway[row][c] == 'O':
                break
            elif hallway[row][c] == 'S':
                return False
    return True

def DFS(placed, pos, hallway, depth):
    global teachers, size
    if depth == 3:
        return isSafe(teachers, hallway, size)

    if pos[1] == size:
        pos = (pos[0]+1, 0)
    if pos[0] == size:
        return False
    row, col = pos
    
    if pos not in placed:
        newHallway = copy.deepcopy(hallway)
        newHallway[row][col] = 'O'
        withBari = DFS(placed, (row, col+1), newHallway, depth+1)
        if withBari: return True
        withoutBari = DFS(placed, (row, col+1), hallway, depth)
        return withBari or withoutBari
    
    return DFS(placed, (row, col+1), hallway, depth)


size = int(input())
hallway = []
teachers = []
students = []
for i in range(size):
    info = list(input().split())
    t = [(i, j) for j, x in enumerate(info) if x == 'T']
    if t: teachers += t
    s = [(i, j) for j, x in enumerate(info) if x == 'S']
    if s: students += s
    hallway.append(info)
visited = set(teachers).union(set(students))
able = DFS(visited, (0, 0), hallway, 0)
print('YES') if able else print('NO')