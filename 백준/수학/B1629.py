def answer(a, b):
    if b == 1:
        return a % C

    if b % 2:
        return (answer(a, b // 2) ** 2) * a % C
    else:
        return (answer(a, b // 2) ** 2) % C


A, B, C = map(int, input().split())
print(answer(A, B))
