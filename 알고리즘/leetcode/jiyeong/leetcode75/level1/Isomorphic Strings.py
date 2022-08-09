# 83 ms	14.7 MB
def sol(s, t):
    # 길이 다르면 F
    if(len(s) != len(t)):
        return False

    dic = dict()
    tset = set()  # value는 겹칠 수 있으니 set에 넣어두고 dict에 이미 저장되어있는지 확인

    for i in range(len(s)):
        if s[i] in dic.keys():
            # key와 value가 다르면 F
            if t[i] != dic.get(s[i]):
                return False
        else:
            # 이미 value로 넣어져 있으면 F
            if t[i] in tset:
                return False

            dic[s[i]] = t[i]
            tset.add(t[i])

    return True


# 108 ms	14.8 MB
def sol2(s, t):
    # 길이 다르면 F
    if(len(s) != len(t)):
        return False

    dic = dict()

    for i in range(len(s)):
        if s[i] in dic.keys():
            # key와 value가 다르면 F
            if t[i] != dic.get(s[i]):
                return False
        else:
            # 이미 value에 있으면 F
            if t[i] in dic.values():
                return False

            dic[s[i]] = t[i]
    return True
