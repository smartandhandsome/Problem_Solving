import sys

input = sys.stdin.readline
N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

pipe = [(0, 1), (1, 0), (1, 1)]
total = 0


def dfs(x, y, direction):
    global total
    if x == N - 1 and y == N - 1 and house[x][y] == 0:
        total += 1
        return
    for n, xy in enumerate(pipe):
        if direction + n == 1:
            continue
        dx, dy = x + xy[0], y + xy[1]
        if dx > N - 1 or dy > N - 1:
            continue
        if (n == 2 and (house[dx - 1][dy] == 1 or house[dx][dy - 1] == 1)) or house[dx][dy] == 1:
            continue
        dfs(dx, dy, n)


dfs(0, 1, 0)
print(total)
