import sys

word = sys.stdin.readline().rstrip()

# 숫자만 추출
re = ""
for i in word:
    if(ord(i) >= ord('0') and ord(i) <= ord('9')):
        re += i
num = int(re)

print(num)

# 숫자만 추출2
# num = 0
# for x in word:
#     # isdecimal() -> 0~9까지 참으로 반환
#     if x.isdecimal():
#         num = num*10+int(x)
# print(num)

# 약수
cnt = 0
for i in range(1, num+1):
    if(num % i == 0):
        cnt += 1

print(cnt)
