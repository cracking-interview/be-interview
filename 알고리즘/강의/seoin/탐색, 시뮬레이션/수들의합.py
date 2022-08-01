import sys

n, m = map(int(sys.stdin.readline().rstrip()))
a = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for i in range(n):
    sum = 0
    sum += a[i]

    if sum == m:
        count += 1
    elif sum < m:
       for j in range(i + 1, n):
           sum += a[j]
           if sum >= m:
               if sum == m:
                    count += 1
               break
    

print(count)


# 예시 코드 - two pointer
n, m=map(int, sys.stdin.readline().rstrip())
a=list(map(int, sys.stdin.readline().rstrip().split()))

lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)
