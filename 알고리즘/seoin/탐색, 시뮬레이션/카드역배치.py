a = list(range(1, 21))

for i in range(10):
    s, e = map(int, input().split())
    s -= 1
    a_ = a[:s] + a[s:e][::-1] + a[e:]
    a = a_

print(a)


# 예시 코드
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

print(a)