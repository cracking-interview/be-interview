def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


n = int(input())
arr = list(map(int, input().split()))
max = 0
answer = 0

for i in arr:
    val = digit_sum(i)
    if max < val:
        max = val
        answer = i

print(answer)
