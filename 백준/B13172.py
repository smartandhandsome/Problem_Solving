M = int(input())
X = 1000000007


def search(b, exp):
    if exp == 1:
        return b
    if exp % 2:
        return search(b, exp - 1) * b
    temp = search(b, exp // 2) % X
    return temp * temp % X


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


total = 0
for _ in range(M):
    N, S = map(int, input().split())
    g = gcd(N, S)
    N //= g
    S //= g
    total += (S * search(N, X - 2) % X)
    total %= X

print(total)
