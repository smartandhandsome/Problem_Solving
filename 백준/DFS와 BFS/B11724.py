"""
https://www.acmicpc.net/problem/11724
"""
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(n, v):
    v.append(n)
    for g in graph[n]:
        if g not in v:
            v.append(g)
            dfs(g, v)


cnt = 0
for i in range(1, N + 1):
    if i not in visit:
        dfs(i, visit)
        cnt += 1
print(cnt)
