"""
https://www.acmicpc.net/problem/1238
다익스트라
"""
from collections import defaultdict
import heapq

N, M, X = map(int, input().split())
graph = defaultdict(list)
graph_r = defaultdict(list)
for middle in range(M):
    S, E, T = map(int, input().split())
    graph[S].append((T, E))
    graph_r[E].append((T, S))


def dijkstra(start, g):
    q = [[0, start]]
    dis = [10000000000] * (N + 1)
    dis[start] = 0
    while q:
        time, node = heapq.heappop(q)
        for t, n in g[node]:
            T = time + t
            if dis[n] > T:
                dis[n] = T
                heapq.heappush(q, [T, n])
    return dis


answer = 0
back = dijkstra(X, graph)
go = dijkstra(X, graph_r)
print(max([back[i] + go[i] for i in range(1, N + 1)]))
