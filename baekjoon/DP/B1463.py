X = int(input())
dp = [0 for _ in range(X + 1)]

for i in range(len(dp)):
    if i < 2:
        continue
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1
print(dp[X])
