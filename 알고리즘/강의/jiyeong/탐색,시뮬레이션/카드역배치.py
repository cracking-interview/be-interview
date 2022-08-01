arr = [i for i in range(1, 21)]

# for i in range(10):
#     store = []
#     s, e = map(int, input().split())
#     store = arr[s-1:e]
#     store.reverse()
#     # print(list(reversed(store)))
#     k = 0
#     for j in range(s-1, e):
#         arr[j] = store[k]
#         k += 1

# for i in arr:
#     print(i, end=' ')

# sol2
for i in range(10):
    s, e = map(int, input().split())
    s -= 1
    arr_ = arr[:s]+arr[s:e][::-1]+arr[e:]
    arr = arr_

for i in arr:
    print(i, end=' ')

# sol3
# a = list(range(21))
# for _ in range(10):
#     s, e = map(int, input().split())
#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i] = a[e-i], a[s+i]
# a.pop(0)
# for x in a:
#     print(x, end=' ')
