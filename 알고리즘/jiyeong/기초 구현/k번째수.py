# T = int(input())

# for t in range(1, T+1):
#     n, s, e, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr2 = []
#     for i in range(s-1, e-1):
#         arr2.append(arr[i])
#     arr2.sort()
#     print("#%d %d" % (t, arr[k-1]))

T = int(input())

for t in range(1, T+1):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    arr.sort()
    print("#%d %d" % (t, arr[k-1]))
