from collections import deque


def BFS():
    visit = [[[0] * 2 for __ in range(M + 1)] for _ in range(N + 1)]
    queue = deque()
    queue.append((1, 1, 0))
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while queue:
        x, y, wall = queue.popleft()
        if x == N and y == M:
            return visit[x][y][wall] + 1
        for i, j in direction:
            a = x + i
            b = y + j
            if a < 1 or a > N or b < 1 or b > M or visit[a][b][wall] != 0:
                continue
            if matrix[a][b] == 0:
                queue.append((a, b, wall))
                visit[a][b][wall] = (visit[x][y][wall] + 1)
            elif matrix[a][b] == 1 and wall == 0:
                queue.append((a, b, 1))
                visit[a][b][1] = (visit[x][y][0] + 1)

    return -1


N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
matrix[0] = [0] * (M + 1)
for i in range(1, N + 1):
    matrix[i] = [0] + list(map(int, input()))

print(BFS())
