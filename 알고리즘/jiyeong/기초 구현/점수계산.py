n = int(input())
arr = list(map(int, input().split()))

cnt = 0
if(arr[0] == 1):
    cnt = 1

tmp = 1
for i in range(1, n):
    if(arr[i] == 1):
        if(arr[i-1] == 1):
            tmp += 1
            cnt += tmp
        else:
            cnt += 1
    else:
        tmp = 1

print(cnt)


# cnt=0
# sum=0
# for i in range(n):
#     if arr[i]==1:
#         cnt=cnt+1
#         sum=sum+cnt
#     else:
#         cnt=0

# print(sum)
