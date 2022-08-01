import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
# k 번째 약수
# N의 약수들 중 K번째로 작은 수
# 존재하지 않을 경우 -1

for i in range(1, n+1):
    if n % i == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)