n = int(input())

def isPrime(x):
    if(x < 2):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


cnt = 0
for i in range(1, n+1):
    if(isPrime(i)):
        # print(i)
        cnt += 1

print(cnt)


# ch = [0]*(n+1)
# cnt = 0
# for i in range(2, n+1):
#     if ch[i] == 0:
#         cnt += 1
#         for j in range(i, n+1, i):
#             ch[j] = 1
# print(cnt)
