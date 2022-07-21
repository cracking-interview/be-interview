n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 행, 열
max_sum = -2149000000
for i in range(0, n):
    sum1, sum2 = 0, 0
    for j in range(0, n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    max_sum = max(sum1, sum2, max_sum)

# 대각선
sum1, sum2 = 0, 0
for i in range(0, n):
    sum1 += a[i][i]
    sum2 += a[i][n-1-i]
max_sum = max(sum1, sum2, max_sum)

print(max_sum)