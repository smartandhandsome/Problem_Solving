N, K = map(int, input().split())
thing_list = []
for _ in range(N):
    W, V = map(int, input().split())
    thing_list.append((W, V))

dp = [[0] * (K + 1) for _ in range(N)]
for i in range(N):
    weight = thing_list[i][0]
    value = thing_list[i][1]
    for j in range(1, K + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], value + dp[i-1][j - weight])
print(dp[N-1][K])
