N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for t in range(N):  # 거쳐가는
    for i in range(N):  # 시작
        for j in range(N):  # 도착
            if graph[i][j] == 0 and (graph[i][t] != 0 and graph[t][j] != 0):
                graph[i][j] = 1

for i in range(N):
    print(*graph[i])
