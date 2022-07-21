n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

# lst.pop()
# 함수의 인자로 0을 주면 0번 인덱스를 삭제하고 하나씩 왼쪽으로 당긴다. 
# 인자로 공백을 주면 가장 마지막 인덱스를 삭제.

# lst.insert(index, value)
# 반드시 삽입할 위치를 명시해야 한다. 
# index 위치에 삽입되면 그 오른쪽의 원소들이 하나씩 오른쪽으로 밀린다.

for i in range(m):
# 첫번째 수는 행번호(h) 
# 두 번째 수는 방향(t) : 0이면 왼쪽, 1이면 오른쪽
# 세 번째 수는 회전하는 격자의 수(k)
    h, t, k = map(int, input().split())
    if (t == 0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

result = 0
s = 0
e = n - 1

for i in range(n):
    for j in range(s, e + 1):
        result += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else: 
        s -= 1
        e += 1

print(result)