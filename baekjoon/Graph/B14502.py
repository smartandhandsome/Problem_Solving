from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
lab = []
virus = []
wall = []
for i in range(N):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(len(row)):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 1:
            wall.append((i, j))
MAX = 0
empty = [(i, j) for i in range(N) for j in range(M) if not (i, j) in virus + wall]
com = combinations(empty, 3)


def bfs():
    queue = deque(virus)
    temp = copy.deepcopy(lab)
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            a = x + dx
            b = y + dy
            if 0 <= a < N and 0 <= b < M:
                if temp[a][b] == 0:
                    temp[a][b] = 1
                    queue.append((a, b))
    cnt = 0
    for t in temp:
        cnt += t.count(0)
    return cnt


for c in com:
    for i, j in c:
        lab[i][j] = 1
    m = bfs()
    if m > MAX:
        MAX = m
    for i, j in c:
        lab[i][j] = 0
print(MAX)
