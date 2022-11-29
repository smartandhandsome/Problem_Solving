import heapq
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
road = [[] for _ in range(N + 1)]
for _ in range(M):
    S, E, W = map(int, input().split())
    road[S].append([W, E])
S, E = map(int, input().split())

dp = [1e9] * (N + 1)
r = [[] for _ in range(N + 1)]
r[S] = []
dp[S] = 0
queue = [[0, S, []]]

while queue:
    weight, node, route = heapq.heappop(queue)
    if weight > dp[node]:
        continue
    for w, e in road[node]:
        if dp[e] > weight + w:
            dp[e] = weight + w
            r[e] = route + [node]
            heapq.heappush(queue, [dp[e], e, r[e]])
ans = r[E] + [E]
print(dp[E])
print(len(ans))
print(*ans)