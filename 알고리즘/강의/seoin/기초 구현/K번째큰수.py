import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))

res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])

res=list(res)
res.sort(reverse=True)
print(res[k-1])