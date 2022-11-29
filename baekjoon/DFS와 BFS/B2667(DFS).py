N = int(input())
graph = []
go = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    graph.append(list(map(int, list(input()))))


def DFS(a, b):
    global cnt
    graph[a][b] = 0
    cnt += 1

    for g in go:
        x = a - g[0]
        y = b - g[1]
        if x < 0 or x >= N or y < 0 or y >= N:
            continue
        if graph[x][y] == 1:
            DFS(x, y)

    return cnt


answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0
            answer.append(DFS(i, j))

print(len(answer))
for ans in sorted(answer):
    print(ans)
