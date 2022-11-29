# 머리가 안돌아감
# 이해는 했지만 막상 구현하라고 하면 못 할 듯

def stars(n):
    if n == 3:
        star[0][:3] = star[2][:3] = [1, 1, 1]
        star[1][:3] = [1, 0, 1]
        return
    n3 = n // 3
    stars(n3)
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            for k in range(n3):
                star[n3 * i + k][n3 * j:n3 * (j + 1)] = star[k][:n3]


N = int(input())
star = [[0] * N for _ in range(N)]
stars(N)
for i in range(N):
    for j in range(N):
        if star[i][j]:
            print('*', end="")
        else:
            print(' ', end="")
    print()
