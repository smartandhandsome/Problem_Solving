import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
nums = []
for i in range(1, N + 1):
    num = 0
    for j in range(1, N + 1):
        if i == j:
            continue
        num += matrix[i][j]
    nums.append(num)
print(nums.index(min(nums)) + 1)
