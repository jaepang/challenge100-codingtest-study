# 2130~2155
import sys
input = sys.stdin.readline

def rotate(arr):
    global height, width
    for depth in range(min(width, height)//2):
        top = depth
        bottom = height-depth-1
        left = depth
        right = width-depth-1
        tmp = arr[top][left]
        for c in range(left+1, right+1):
            arr[top][c-1] = arr[top][c]
        for r in range(top+1, bottom+1):
            arr[r-1][right] = arr[r][right]
        for c in reversed(range(left, right)):
            arr[bottom][c+1] = arr[bottom][c]
        for r in reversed(range(top, bottom)):
            arr[r+1][left] = arr[r][left]
        arr[top+1][left] = tmp

height, width, rotates = list(map(int, input().split()))
arr = []
for _ in range(height):
    arr.append(list(map(int, input().split())))

for _ in range(rotates):
    rotate(arr)
for row in arr:
    for point in row:
        print(point, end=' ')
    print()
