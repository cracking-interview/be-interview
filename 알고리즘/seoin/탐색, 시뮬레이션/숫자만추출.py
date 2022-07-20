# 내 풀이
str = input()
size = len(str)

nums = ""
# 48-57
for i in range(size):
    if (ord(str[i]) in range(48, 58)):
        nums += str[i]

nums = int(nums)
count = 0

for i in range(1, nums + 1):
    if nums % i == 0:
        count += 1

print(nums)
print(count)


# 예시 풀이

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0

for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)