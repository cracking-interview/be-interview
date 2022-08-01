import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

# python - round_half_even 채택
# 짝수인 정수로 반올림
# 4.5000 -> 4
# 4.5111 -> 5
# 5.5000 -> 6
AVG =  round(sum(a) / n + 0.5)

min = float('inf')
for idx, x in enumerate(a):
    tmp = abs(x - AVG)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(AVG, res)