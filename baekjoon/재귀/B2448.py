N = int(input())
matrix = [[' '] * (N * 2) for _ in range(N)]


def star(N, a, b):
    if N == 3:
        matrix[a][b + 2] = "*"
        matrix[a + 1][b + 1] = matrix[a + 1][b + 3] = "*"
        for i in range(5):
            matrix[a + 2][b + i] = "*"
        return

    star(N // 2, a, b + (N // 2))
    star(N // 2, a + (N // 2), b)
    star(N // 2, a + (N // 2), b + N)


star(N, 0, 0)
for m in matrix:
    print("".join(m))
