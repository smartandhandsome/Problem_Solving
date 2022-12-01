from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
dp = [float("INF")] * (V + 1)
dp[K] = 0

heap = [(0, K)]
while heap:
    weigh, node = heapq.heappop(heap)
    if weigh > dp[node]:
        continue
    for t, idx in graph[node]:
        w = t + weigh
        if dp[idx] > w:
            dp[idx] = w
            heapq.heappush(heap, (w, idx))
for i in range(1, V+1):
    print(dp[i] if dp[i] != float('inf') else "INF")
