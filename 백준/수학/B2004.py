def two(n):
    two = 0
    while n != 0:
        n //= 2
        two += n
    return two


def five(n):
    five = 0
    while n != 0:
        n //= 5
        five += n
    return five


N, M = map(int, input().split())

print(min(two(N) - two(N - M) - two(M), five(N) - five(N - M) - five(M)))
