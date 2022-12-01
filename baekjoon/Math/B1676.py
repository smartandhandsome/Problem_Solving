def two(N):
    t = 0
    while N != 0:
        N //= 2
        t += N
    return t


def five(N):
    f = 0
    while N != 0:
        N //= 5
        f += N
    return f


N = int(input())

print(min(two(N), five(N)))
