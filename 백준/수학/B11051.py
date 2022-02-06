N, K = map(int, input().split())
dp = [[1] for _ in range(N + 1)]
dp[1].append(1)

for i in range(2, N + 1):
    for j in range(1, i + 1):
        if i == j:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
print(dp[N][K] % 10007)