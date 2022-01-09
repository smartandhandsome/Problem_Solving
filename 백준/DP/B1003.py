T = int(input())

for _ in range(T):
    num = int(input())
    dp = [[0, 0]] * (num + 1)
    for n in range(num + 1):
        if n == 0:
            dp[0] = [1, 0]
        elif n == 1:
            dp[1] = [0, 1]
        elif dp[n] == [0, 0]:
            dp[n] = [dp[n - 1][0] + dp[n - 2][0], dp[n - 1][1] + dp[n - 2][1]]
    for n in dp[num]:
        print(n, end=" ")
    print()
