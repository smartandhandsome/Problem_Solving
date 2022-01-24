"""
https://www.acmicpc.net/problem/17626
"""
N = int(input())
dp = [float('inf')] * (N + 1)
dp[0] = 0
for idx in range(1, N + 1):
    s = idx ** (1 / 2)
    if (idx ** 0.5).is_integer():
        dp[idx] = 1
    else:
        for i in range(1, int(idx ** 0.5) + 1):
            dp[idx] = min(dp[idx], dp[i * i] + dp[idx - i * i])
print(dp[N])
