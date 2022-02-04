"""
https://www.acmicpc.net/problem/16928
dp 풀이 (틀림)
이 문제를 dp로 못 푸는 이유
DAG가 아니기 때문이다.
뒤로 돌아가는 경우가 있고 뒤로 돌아갔을 경우 더 빠르게 도착할 수 있음.
"""
from collections import deque
visit = [False] * 101
load = [0] * 101
L, S = map(int, input().split())
ladder = {}
snake = {}
for _ in range(L):
    s, e = map(int, input().split())
    ladder[s] = e
for _ in range(S):
    s, e = map(int, input().split())
    snake[s] = e
queue = deque()
visit[1] = True
queue.append(1)
while queue:
    location = queue.popleft()
    if location == 100:
        break
    for n in [1, 2, 3, 4, 5, 6]:
        move = location + n
        if move <= 100 and not visit[move]:
            if move in ladder:
                move = ladder[move]
            if move in snake:
                move = snake[move]
            if not visit[move]:
                queue.append(move)
                visit[move] = True
                load[move] = load[location] + 1

print(load[100])
