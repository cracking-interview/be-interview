n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = 1
sum = arr[0]
cnt = 0
while True:
    if sum < m:
        if rt < n:
            sum += arr[rt]
            rt += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= arr[lt]
        lt += 1
    else:
        sum -= arr[lt]
        lt += 1
print(cnt)
