import sys

n, m = map(int, sys.stdin.readline().rstrip().split()))
a = [0] * (n+m+1)

for i in range(1, n):
    for j in range(1, m):
        a[i+j] +=1

cnt=[0]*(n+m+3)
max=0
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]=cnt[i+j]+1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
    
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')