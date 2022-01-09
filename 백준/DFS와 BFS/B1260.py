N, M, V = map(int, input().split())
graph = {}

for i in range(1, N + 1):
    graph[i] = set()

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

for i in range(1, N + 1):
    graph[i] = sorted(list(graph[i]))


def dfs(v):
    visit[v] = True
    print(v, end=" ")
    for n in graph[v]:
        if not visit[n]:
            dfs(n)


def bfs(v):
    queue = [v]
    visit[v] = True
    while queue:
        p = queue.pop(0)
        print(p, end=" ")
        for n in graph[p]:
            if not visit[n]:
                visit[n] = True
                queue.append(n)


visit = [False] * (N + 1)
start = 1
dfs(V)
print()

visit = [False] * (N + 1)
start = 1
bfs(V)
