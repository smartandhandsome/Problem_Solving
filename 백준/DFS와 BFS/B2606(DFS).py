V_num = int(input())
E_num = int(input())
graph = [[0] * (V_num + 1) for _ in range(V_num + 1)]

for _ in range(E_num):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visit = [False] * (V_num + 1)
cnt = 0


def DFS(v):
    global cnt
    visit[v] = True
    for i in range(1, len(graph[v])):
        if graph[v][i] == 1 and not visit[i]:
            cnt += 1
            DFS(i)

    return cnt


print(DFS(1))
