# return 타입이 뭔지 확인할것!

arr = set()
for i in nums:
    if i in arr:
        return True
    else:
        arr.add(i)
else:
    return False