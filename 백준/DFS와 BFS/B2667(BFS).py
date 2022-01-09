from collections import deque

N = int(input())
graph = []
go = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    graph.append(list(map(int, list(input()))))


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        p = queue.popleft()
        for g in go:
            px = p[0] + g[0]
            py = p[1] + g[1]

            if px < 0 or px >= N or py < 0 or py >= N:
                continue
            if graph[px][py] == 1:
                graph[px][py] = 0
                queue.append((px, py))
                cnt += 1

    return cnt


c = 0
cnt_list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt_list.append(BFS(i, j))
            c += 1

print(c)
for n in sorted(cnt_list):
    print(n)
