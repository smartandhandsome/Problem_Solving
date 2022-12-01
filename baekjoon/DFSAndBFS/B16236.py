import heapq

N = int(input())
m = []
q = []
for i in range(N):
    li = list(map(int, input().split()))
    if 9 in li:
        location = (i, li.index(9))
    m.append(li)
m[location[0]][location[1]] = 0
q.append((0, location[0], location[1]))
size = 2
exp = 0
total = 0
visit = [[False] * N for _ in range(N)]
while q:
    d, x, y = heapq.heappop(q)
    if 0 < m[x][y] < size:
        exp += 1
        if exp == size:
            size += 1
            exp = 0
        m[x][y] = 0
        total += d
        d = 0
        while q:
            q.pop()
        visit = [[False] * N for _ in range(N)]
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        nd, nx, ny = d + 1, x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if m[nx][ny] <= size and not visit[nx][ny]:
                heapq.heappush(q, (nd, nx, ny))
                visit[nx][ny] = True
print(total)
