n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    r, dir, k = map(int, input().split())
    if(dir == 0):
        for _ in range(k):
            arr[r-1].append(arr[r-1].pop(0))
    else:
        for _ in range(k):
            arr[r-1].insert(0, arr[r-1].pop())

answer = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        answer += arr[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(answer)
