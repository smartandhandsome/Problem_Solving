from collections import deque

N, K = map(int, input().split())
q = deque([N])
visit = [[-1, 0] for _ in range(100001)]

visit[N][0] = 0
visit[N][1] = 1
while q:
    location = q.popleft()
    for x in [location + 1, location - 1, location * 2]:
        if 0 <= x <= 100000:
            if visit[x][0] == -1:
                visit[x][0] = visit[location][0] + 1
                visit[x][1] = visit[location][1]
                q.append(x)
            elif visit[location][0] + 1 == visit[x][0]:
                visit[x][1] += visit[location][1]

print(visit[K][0])
print(visit[K][1])
