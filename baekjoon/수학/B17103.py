import sys

input = sys.stdin.readline
T = int(input())
nums = [int(input()) for _ in range(T)]
M = max(nums)
primes = [False, False] + [True] * (M - 1)

for i in range(2, int(M ** 0.5) + 1):
    if primes[i]:
        for j in range(i * 2, M + 1, i):
            if primes[j]:
                primes[j] = False
for N in nums:
    cnt = 0
    for i in range(2, N // 2 + 1):
        if primes[i] and primes[N - i]:
            cnt += 1

    print(cnt)
