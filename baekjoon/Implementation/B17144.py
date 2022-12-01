R, C, T = map(int, input().split())
room = []
air_cleaner = []
for i in range(R):
    room.append(list(map(int, input().split())))
top = -1
down = -1
for i in range(R):
    if room[i][0] == -1:
        top = i
        break
down = top + 1


def spread():
    temp = [[0] * C for _ in range(R)]
    temp[top][0] = -1
    temp[down][0] = -1

    for x in range(R):
        for y in range(C):
            if room[x][y] != 0 and room[x][y] != -1:
                cnt = 0
                for dx, dy in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                    if 0 <= dx < R and 0 <= dy < C:
                        if room[dx][dy] != -1:
                            temp[dx][dy] += room[x][y] // 5
                            cnt += 1
                temp[x][y] += room[x][y] - (room[x][y] // 5 * cnt)
    return temp


def move(w, a, b):
    direct = 0
    prev = 0
    x, y = w, 1
    while True:
        dx = x + a[direct]
        dy = y + b[direct]
        if dx == w and dy == 0:
            room[x][y], prev = prev, room[x][y]
            break
        if 0 > dx or dx >= R or 0 > dy or dy >= C:
            direct += 1
            continue
        room[x][y], prev = prev, room[x][y]
        x, y = dx, dy


for _ in range(T):
    room = spread()
    move(top, [0, -1, 0, 1], [1, 0, -1, 0])
    move(down, [0, 1, 0, -1], [1, 0, -1, 0])
total = 0
for r in room:
    total += sum(r)
print(total + 2)
