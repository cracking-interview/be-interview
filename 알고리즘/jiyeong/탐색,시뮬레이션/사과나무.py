n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

# sum = 0
# tmp = n//2

# for i in range(n):
#     sum += map[i][tmp]

# for i in range(1, tmp+1): # 0 1 2
#     for j in range(n): # 0 1 2 3 4 5 6
#         print()


res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += map[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
