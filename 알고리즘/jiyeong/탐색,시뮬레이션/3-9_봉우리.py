n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]
map.insert(0, [0]*n)
map.append([0]*n)

for i in map:
    i.insert(0, 0)
    i.append(0)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(map[i][j] > map[i+dx[k]][j+dy[k]]for k in range(4)):
            cnt += 1

print(cnt)
