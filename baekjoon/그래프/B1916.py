import heapq, sys

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, W = map(int, input().split())
    heapq.heappush(graph[S], (W, E))
start, target = map(int, input().split())
queue = [(0, start)]
dp = [1e9] * (N + 1)
while queue:
    w, n = heapq.heappop(queue)
    for weight, node in graph[n]:
        if dp[node] > w + weight:
            dp[node] = w + weight
            heapq.heappush(queue, (dp[node], node))

print(dp[target])