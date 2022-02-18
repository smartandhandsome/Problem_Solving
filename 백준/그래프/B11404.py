"""
https://www.acmicpc.net/problem/11404
"""
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if k == i or k == j or i == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(graph[i][j] if graph[i][j] != float('inf') else 0, end=" ")
    print()
