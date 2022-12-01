"""
https://www.acmicpc.net/problem/1167
1. x부터 가장 먼 노드 구함(y)
2. y에서 가장 먼 노드 구함(z)
3. y - z 거리가 트리의 지름
"""
import sys

input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N + 1)]
for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(1, len(line) - 2, 2):
        graph[line[0]].append((line[i], line[i + 1]))


def dfs(x, score):
    for target, s in graph[x]:
        if score[target] == -1:
            score[target] = score[x] + s
            dfs(target, score)


now_long = [-1] * (N + 1)
now_long[1] = 0
dfs(1, now_long)
idx = now_long.index(max(now_long))
longest = [-1] * (N + 1)
longest[idx] = 0
dfs(idx, longest)
print(max(longest))
