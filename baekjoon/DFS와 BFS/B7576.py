from collections import deque

M, N = map(int, input().split())
tomato = []
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(N):
    tomato.append(list(map(int, input().split())))


def BFS(l):
    queue = deque()
    queue.extend(l)

    while queue:
        x, y = queue.popleft()
        for di in direc:
            dx = x + di[0]
            dy = y + di[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if tomato[dx][dy] == 0:
                tomato[dx][dy] = tomato[x][y] + 1
                day = tomato[dx][dy]
                queue.append((dx, dy))


location = []

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            location.append((i, j))
BFS(location)
check = False
answer = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
    answer = max(max(tomato[i]), answer)
print(answer - 1)
