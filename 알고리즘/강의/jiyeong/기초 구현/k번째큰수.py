from itertools import combinations

n, k = map(int, input().split())

arr = list(combinations(list(map(int, input().split())), 3))
tmp = set()

for i in range(len(arr)):
    sum = 0
    for j in range(3):
        sum += arr[i][j]
    tmp.add(sum)

tmp = list(tmp)
tmp.sort(reverse=True)
print(tmp[k-1])
