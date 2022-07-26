map = [list(map(int, input().split())) for _ in range(9)]


def check(a):
    for i in range(9):
        rchk = [0]*10
        cchk = [0]*10
        for j in range(9):
            if rchk[map[i][j]] == 0:
                rchk[map[i][j]] = 1
            else:
                return False

            if cchk[map[j][i]] == 0:
                cchk[map[j][i]] = 1
            else:
                return False

    for i in range(3):
        for j in range(3):
            schk = [0]*10
            for k in range(3):
                for s in range(3):
                    if schk[map[i*3+k][j*3+s]] == 0:
                        schk[map[i*3+k][j*3+s]] = 1
                    else:
                        return False

    return True


if check(map):
    print("YES")
else:
    print("NO")
