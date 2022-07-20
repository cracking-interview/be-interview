import sys

n = int(input())

for i in range(1, n+1):
    word = sys.stdin.readline().rstrip().upper()
    # 문자열 뒤집기
    rword = word[::-1]
    if word == rword:
        print("#%d YES" % i)
    else:
        print("#%d NO" % i)

# 사이즈를 반으로 나눠 반만 비교
# for i in range(1, n+1):
#     str=input()
#     str=str.upper()
#     for j in range(len(str)//2):
#         if str[j]!=str[-1-j]:
#             print("#%d NO" %i)
#             break
#     else:
#         print("#%d YES" %i)
