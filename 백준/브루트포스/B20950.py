from itertools import combinations

N = int(input())
color = [tuple(map(int, input().split())) for _ in range(N)]

ans = 1e9

R_gom, G_gom, B_gom = map(int, input().split())

for i in range(2, min(N, 7) + 1):
    for com in combinations(color, i):
        x, y, z = 0, 0, 0
        k = len(com)
        for R, G, B in com:
            x += R
            y += G
            z += B
        ans = min(ans, abs(R_gom - x // k) + abs(G_gom - y // k) + abs(B_gom - z // k))
print(ans)
