"""
https://www.acmicpc.net/problem/1865
벨만 포드
"""
T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    road = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        road[S].append((T, E))
        road[E].append((T, S))
    for _ in range(W):
        S, E, T = map(int, input().split())
        road[S].append((-T, E))
    dp = [10001] * (N + 1)
    for c in range(1, N + 1):
        for Route in range(1, N + 1):
            for w, node in road[Route]:
                if dp[node] > dp[Route] + w:
                    dp[node] = dp[Route] + w
                    if c == N:
                        print("YES")
                        exit()

    print("NO")
