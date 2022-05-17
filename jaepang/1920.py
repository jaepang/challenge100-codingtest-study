def bSearch(arr, tar):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        
        if arr[mid] == tar:
            return 1
        elif arr[mid] > tar:
            end = mid-1
        else:
            start = mid+1
    
    return 0

n = int(input())
a = list(map(int, input().split()))

a.sort()
m = int(input())
b = list(map(int, input().split()))
for i in b:
    print(bSearch(a, i))