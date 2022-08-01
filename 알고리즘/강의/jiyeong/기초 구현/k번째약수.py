# n의 약수들 중 k번째로 작은 수를 출력하시오.

# n, k = map(int, input().split())

# arr = [0] * (n+1)
# t = 0

# for i in range(1, n+1):
#     if(n % i == 0):
#         arr[t] = i
#         t += 1

# if arr[k-1] == 0:
#     print(-1)
# else:
#     print(arr[k-1])


n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if(n % i == 0):
        cnt += 1

    if cnt == k:
        print(i)
        break

else:
    print(-1)
