# 이분탐색 풀이

import bisect

N = int(input())
line = []

for _ in range(N):
    line.append(tuple(map(int, input().split())))

line.sort()
dp = [line[0][1]]

for i in range(1, N):
    if line[i][1] > dp[-1]:
        dp.append(line[i][1])
    else:
        idx = bisect.bisect_left(dp, line[i][1])
        dp[idx] = line[i][1]

print(N - len(dp))
