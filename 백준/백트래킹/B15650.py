N, M = map(int, input().split())
l = []


def dfs(x):
    if len(l) == M:
        print(*l)

    for i in range(x, N + 1):
        l.append(i)
        dfs(i + 1)
        l.pop()


dfs(1)
