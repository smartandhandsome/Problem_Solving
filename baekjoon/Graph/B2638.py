"""
https://www.acmicpc.net/problem/2638
"""
from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))


def bfs():
    queue = deque([(0, 0)])
    visit = [[False] * M for _ in range(N)]
    visit[0][0] = True
    while queue:
        a, b = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x = dx + a
            y = dy + b
            if 0 <= x < N and 0 <= y < M and not visit[x][y] and cheese[x][y] != 1:
                queue.append((x, y))
                cheese[x][y] = 10
                visit[x][y] = True


def check(a, b):
    total = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = a + dx, b + dy
        total += cheese[x][y]
    if total // 10 >= 2:
        return True
    return False


def HaveOne():
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                return True
    return False


def time_():
    time = 0
    flag = True
    while flag:
        bfs()
        for i in range(N):
            for j in range(M):
                if cheese[i][j] == 1 and check(i, j):
                    cheese[i][j] = 0
        time += 1
        flag = HaveOne()

    return time


print(time_())
