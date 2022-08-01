# 일일이 비교하는 것은 시간초과
# 최저를 가장 먼저 구하는 것은 잘못된 답 ex) [2,4,1]

maximum = 0
minimum = sys.maxsize

for i in prices:
    minimum = min(minimum, i)
    maximum = max(maximum, i-minimum)

print(maximum)