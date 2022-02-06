"""
https://www.acmicpc.net/problem/11401
1. 페르마의 소정리
2. 고속거듭제곱 O(logN)
"""
N, K = map(int, input().split())
p = 1000000007
factorial = [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    factorial[i] = factorial[i - 1] * i % p


def square(x, y):
    if y == 0:
        return 1
    answer = 1
    if y % 2:
        answer *= x
    half = square(x, y // 2)
    return answer * half * half % p


top = factorial[N]
bottom = (factorial[K] * factorial[N - K]) % p
print((top * square(bottom, p - 2)) % p)
