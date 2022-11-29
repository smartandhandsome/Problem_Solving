N, M = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
total_cost = (sum(cost) + 1)
dp = [[0] * total_cost for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(total_cost):
        if j < cost[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])

for j in range(total_cost):
    for i in range(1, N + 1):
        if dp[i][j] >= M:
            print(j)
            exit()
