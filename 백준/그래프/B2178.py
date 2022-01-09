moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input())))


def search():
    queue = [[0, 0]]
    while queue:
        x, y = queue.pop(0)

        for a, b in moves:
            if x + a < 0 or x + a >= N or y + b < 0 or y + b >= M:
                continue

            if Map[x + a][y + b] == 1:
                queue.append([x + a, y + b])
                Map[x + a][y + b] = Map[x][y] + 1


search()
print(Map[N - 1][M - 1])
