n = int(input())

arr = list(map(int, input().split()))
# round -> round_half_even
# 4.5 -> 4(짝수쪽으로 변경)
# 4.511 -> 5(정확히 반보다 조금이라도 크면 올려줌)
# 5.5 -> 6(짝수쪽으로 변경)

avg = round(sum(arr)/n)

min = float('inf')
tmp = 0
for i in range(len(arr)):
    if(min > abs(avg-arr[i])):
        min = abs(avg-arr[i])
        tmp = i
    elif(min == abs(avg-arr[i])):
        if(arr[tmp] < arr[i]):
            tmp = i

print(avg, tmp+1)
