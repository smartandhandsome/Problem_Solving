def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


M, N = map(int, input().split())
m = GCD(max(M, N), min(M, N))
print(m)
print(M * N // m)
