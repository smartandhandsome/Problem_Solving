N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = 0
    for j in range(1, N + 1):
        dp[i][j] = min(dp[i - 1][j], cards[i] + dp[i][j - i])
print(dp[N][N])
