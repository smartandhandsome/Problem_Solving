from collections import deque


def DFS():
    queue = deque()
    queue.append((myx, myy))

    while queue:
        x, y = queue.popleft()
        if x == dex and y == dey:
            print(chess[x][y])
            return
        for m in move:
            a = x - m[0]
            b = y - m[1]
            if a < 0 or a >= N or b < 0 or b >= N:
                continue

            if chess[a][b] == 0:
                chess[a][b] = chess[x][y] + 1
                queue.append((a, b))


T = int(input())
move = [(-2, 1), (-1, 2), (1, 2), (2, 1),
        (2, -1), (1, -2), (-1, -2), (-2, -1)]
for _ in range(T):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    myx, myy = map(int, input().split())
    dex, dey = map(int, input().split())

    DFS()
