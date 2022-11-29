N = int(input())
color = [tuple(map(int, input().split())) for _ in range(N)]
ans = 1e9
for i in range(3):
    dp = [[1e9] * 3 for _ in range(N)]
    dp[0][i] = color[0][i]
    for j in range(1, N):
        dp[j][0] = color[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = color[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = color[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)