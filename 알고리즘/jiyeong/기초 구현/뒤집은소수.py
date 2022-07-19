n = int(input())
arr = list(map(int, input().split()))


def reverse(x):
    num = ''
    while x > 0:
        num += str(x % 10)
        x //= 10
    return num


def isPrime(x):
    if(x < 2):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


for i in arr:
    val = int(reverse(i))
    if(isPrime(val)):
        print(val, end=' ')
