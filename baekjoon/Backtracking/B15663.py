N, M = map(int, input().split())
nums = list(map(int, input().split()))
buf_list = set()
visit = [False] * N


def backtracking(n, buf):
    if n == 0:
        buf_list.add(tuple(buf))
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            backtracking(n - 1, buf + [nums[i]])
            visit[i] = False


backtracking(M, [])
for l in sorted(buf_list):
    print(*l)
