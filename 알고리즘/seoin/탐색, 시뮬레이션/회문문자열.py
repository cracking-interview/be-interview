# 내 풀이
n = int(input())

def isPalindrome(word):
    return word == word[::-1]

for i in range(n):
    a = input().lower()
    if isPalindrome(a) == True:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))



# 다른 풀이
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)

    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))