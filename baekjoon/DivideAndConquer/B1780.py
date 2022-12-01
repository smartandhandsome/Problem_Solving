import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

cnt = [0, 0, 0]


def cutting(a, b, n):
    num = paper[a][b]
    for i in range(a, a + n):
        for j in range(b, b + n):
            if paper[i][j] != num:
                for x in range(a, a + n, n // 3):
                    for y in range(b, b + n, n // 3):
                        cutting(x, y, n // 3)
                return
    cnt[num] += 1


cutting(0, 0, N)
for i in [-1, 0, 1]:
    print(cnt[i])
