import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


def multiply_matrix(a, b):
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] += a[i][k] * b[k][j]
            ans[i][j] %= 1000
    return ans


def div(a, b):
    if b == 1:
        return a
    t = div(a, b // 2)
    if b % 2:
        return multiply_matrix(multiply_matrix(t, t), a)
    else:
        return multiply_matrix(t, t)


result = div(matrix, M)
for res in result:
    for r in res:
        print(r % 1000, end=" ")
    print()
