N = int(input())

nums_list = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if nums_list[i] > nums_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
