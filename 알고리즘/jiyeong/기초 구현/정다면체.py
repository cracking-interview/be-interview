n, m = map(int, input().split())

arr = [0]*(n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j] += 1

arr2 = arr.copy()
arr2.sort()
maxv = arr2[n+m-1]

for i in range(len(arr)):
    if(arr[i] == maxv):
        print(i, end=' ')
