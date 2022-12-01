from collections import deque

N, K = map(int, input().split())
MAX = 100000
location = [0] * (MAX + 1)


def DFS():
    queue = deque()
    queue.append(N)
    while queue:
        go = queue.popleft()
        if go == K:
            return location[go]
        for i in (go - 1, go + 1, go * 2):
            if 0 <= i <= MAX and not location[i]:
                location[i] = location[go] + 1
                queue.append(i)


print(DFS())
