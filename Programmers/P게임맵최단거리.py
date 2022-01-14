from collections import deque


def solution(maps):
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            a = x + dx
            b = y + dy
            if 0 <= a < len(maps) and 0 <= b < len(maps[0]) and maps[a][b] == 1:
                maps[a][b] = maps[x][y] + 1
                queue.append((a, b))
                if a == len(maps) - 1 and b == len(maps[0]) - 1:
                    return maps[a][b]
    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
