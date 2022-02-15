N = int(input())
M = 1000000007


def matrix_mul(x, y):
    t = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            element = 0
            for k in range(2):
                element += x[i][k] * y[k][j]
            t[i][j] = element % M
    return t


def divide(x, s):
    if s == 1:
        return x
    if s % 2:
        return matrix_mul(divide(x, s - 1), x)
    else:
        return divide(matrix_mul(x, x), s // 2)


matrix = [[1, 1], [1, 0]]
if N == 1:
    print(1)
else:
    print(divide(matrix, N - 1)[0][0])
