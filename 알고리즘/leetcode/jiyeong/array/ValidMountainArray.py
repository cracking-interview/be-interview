def sol(arr):
    up = True
    cnt = 0
    # arr 길이가 3보다 작거나 첫 시작이 잘못되었을 경우(내려가거나 같거나)
    if len(arr) < 3 or arr[0] >= arr[1]:
        return False

    for i in range(2, len(arr)):
        # 두수가 같을 경우
        if arr[i] == arr[i-1]:
            return False
        # 내려가는 경우
        elif arr[i] < arr[i-1]:
            # 한번도 올라가지 않았다가 내려가는 경우
            if cnt == 0:
                # 내려감(False)으로 표시, cnt값 올리기
                up = False
                cnt += 1
        # 또 올라가는 경우
        elif arr[i] > arr[i-1] and cnt != 0:
            return False

    if up:  # 올라가기만 했다면 False
        return False
    else:
        return True