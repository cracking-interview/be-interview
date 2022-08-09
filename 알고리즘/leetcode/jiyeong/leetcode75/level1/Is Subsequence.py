# 19 ms	13.5 MB
def sol(s, t):

    if len(s) == 0:
        return True

    idx = 0
    for i in t:
        if i == s[idx]:
            idx += 1

            if idx == len(s):
                return True
    return False