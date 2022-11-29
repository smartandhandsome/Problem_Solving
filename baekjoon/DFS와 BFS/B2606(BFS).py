V_num = int(input())
E_num = int(input())
graph = [[0] * (V_num + 1) for _ in range(V_num + 1)]

for _ in range(E_num):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def BFS():
    start = 1
    queue = [start]
    visit = [False] * (V_num + 1)
    visit[1] = True
    cnt = 0

    while queue:
        v = queue.pop(0)
        for i in range(1, V_num + 1):
            if graph[v][i] == 1 and not visit[i]:
                queue.append(i)
                visit[i] = True
                cnt += 1

    return cnt


print(BFS())
