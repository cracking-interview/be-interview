import sys

# 내 풀이
n = int(sys.stdin.readline().rstrip())

def isPalindrome(word):
    return word == word[::-1]

for i in range(n):
    a = sys.stdin.readline().rstrip().lower()
    if isPalindrome(a) == True:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))



# 다른 풀이
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    s=sys.stdin.readline().rstrip()
    s=s.upper()
    size=len(s)

    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))