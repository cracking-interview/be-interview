import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

def digit_sum(n):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000

for x in a:
    t = digit_sum(x)
    if t > max:
        max = t
        res = x

print(res)