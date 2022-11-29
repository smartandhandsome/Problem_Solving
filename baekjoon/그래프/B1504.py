import sys, heapq

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    S, E, W = map(int, input().split())
    heapq.heappush(graph[S], [W, E])
    heapq.heappush(graph[E], [W, S])
must_v1, must_v2 = map(int, input().split())


def dijkstra(x):
    queue = [[0, x]]
    dp = [1e9] * (N + 1)
    dp[x] = 0
    while queue:
        w, n = heapq.heappop(queue)
        for weight, node in graph[n]:
            if dp[node] > w + weight:
                dp[node] = w + weight
                heapq.heappush(queue, [dp[node], node])
    return dp


num1_route = dijkstra(1)
v1_route = dijkstra(must_v1)
v2_route = dijkstra(must_v2)
answer = min(num1_route[must_v1] + v1_route[must_v2] + v2_route[N],
             num1_route[must_v2] + v2_route[must_v1] + v1_route[N])
print(-1 if answer >= 1e9 else answer)
