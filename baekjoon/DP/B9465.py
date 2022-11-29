T = int(input())
for _ in range(T):
    N = int(input())
    sticker = []
    for i in range(2):
        sticker.append([0] + list(map(int, input().split())))
    for i in range(2, N + 1):
        sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
        sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
    print(max(sticker[0][N], sticker[1][N]))