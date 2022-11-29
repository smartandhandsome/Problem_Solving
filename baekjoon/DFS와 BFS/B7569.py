"""
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
"""
from collections import deque

M, N, H = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        matrix[i][j] = list(map(int, input().split()))


def BFS():
    while queue:
        a, b, c = queue.popleft()
        for dx, dy, dz in ((0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)):
            x, y, z = a + dx, b + dy, c + dz
            if x < 0 or x >= H or y < 0 or y >= N or z < 0 or z >= M or matrix[x][y][z] != 0:
                continue
            matrix[x][y][z] = matrix[a][b][c] + 1
            queue.append((x, y, z))


queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))
BFS()
ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 0:
                print(-1)
                exit()
        ans = max(ans, max(matrix[i][j]))
print(ans - 1)
