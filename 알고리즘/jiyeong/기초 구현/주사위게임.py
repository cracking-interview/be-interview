n = int(input())

max = 0
money = 0
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    # a = arr[0]
    # b = arr[1]
    # c = arr[2]
    a, b, c = map(int, arr)

    if a == b and b == c:
        money = 10000+a*1000
    elif a == b and b != c:
        money = 1000+a*100
    elif a != b and b == c:
        money = 1000+b*100
    else:
        mondey = c*100

max = money if money > max else max
print(max)
