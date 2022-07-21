n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

xsum = [0 for _ in range(n)]
ysum = [0 for _ in range(n)]
csum = [0 for _ in range(n)]

for i in range(n):
    x = 0
    y = 0
    for j in range(n):
        x += map[i][j]
        y += map[j][i]
    xsum[i] = x
    ysum[i] = y

cross1 = 0
cross2 = 0
for i in range(n):
    cross1 += map[i][i]
    cross2 += map[i][n-1-i]


answer = max(max(xsum), max(ysum), max(cross1, cross2))
print(answer)
