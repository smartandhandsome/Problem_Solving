N = int(input())
cup = [0]
for _ in range(N):
    cup.append(int(input()))
dp = [0, cup[1]]
if N >= 2:
    dp.append(cup[1] + cup[2])

for i in range(3, N + 1):
    dp.append(max(cup[i] + dp[i - 2], cup[i] + cup[i - 1] + dp[i - 3], dp[i - 1]))
print(dp[N])
