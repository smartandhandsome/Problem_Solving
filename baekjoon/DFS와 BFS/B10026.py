from collections import deque

N = int(input())
painting = []
visit = [[False] * N for _ in range(N)]
blind_visit = [[False] * N for _ in range(N)]
for _ in range(N):
    painting.append(list(input()))


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    color = painting[i][j]
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            a, b = x + dx, y + dy
            if 0 <= a < N and 0 <= b < N and not visit[a][b] and painting[a][b] == color:
                visit[a][b] = True
                q.append((a, b))


def b_bfs(i, j):
    q = deque()
    q.append((i, j))
    blind_visit[i][j] = True
    color = [painting[i][j]]
    if 'R' in color:
        color.append('G')
    elif 'G' in color:
        color.append('R')
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            a, b = x + dx, y + dy
            if 0 <= a < N and 0 <= b < N and not blind_visit[a][b] and painting[a][b] in color:
                blind_visit[a][b] = True
                q.append((a, b))


cnt = 0
b_cnt = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            bfs(i, j)
            cnt += 1
        if not blind_visit[i][j]:
            b_bfs(i, j)
            b_cnt += 1

print(cnt, b_cnt)
