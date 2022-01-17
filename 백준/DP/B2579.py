"""
https://www.acmicpc.net/problem/2579
"""
import sys

N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline()))
dp = [0, stair[1]]
if N > 1:
    dp.append(stair[1] + stair[2])
for i in range(3, N + 1):
    dp.append(max(dp[i - 3] + stair[i - 1], dp[i - 2]) + stair[i])
print(dp[N])