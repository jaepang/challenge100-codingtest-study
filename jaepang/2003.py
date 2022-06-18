n, m = map(int, input().split())
arr = list(map(int ,input().split()))

ans = 0
for i in range(n):
    add = arr[i]
    for j in range(i, n):
        add = add + arr[j] if j > i else add
        if add > m:
            break
        elif add == m:
            ans += 1
            break

print(ans)