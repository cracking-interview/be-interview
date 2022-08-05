def sol(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            if 0 in arr:
                return True
        if i*2 in arr:
            return True
    else:
        return False


# 느림
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]*2 or arr[i] * 2 == arr[j]:
#             return True
# else:
#     return False
