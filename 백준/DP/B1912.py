N = int(input())
num_list = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])
print(max(dp[1:]))