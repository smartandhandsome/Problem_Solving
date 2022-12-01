from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
house = []
chicken = []
city = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if r == 1:
            house.append((i, j))
        elif r == 2:
            chicken.append((i, j))
    city.append(row)
chicken_choice = combinations(chicken, M)
MIN = 1e9
for chick in chicken_choice:
    distance = 0
    for h in house:
        shortest = 1e9
        for c in chick:
            shortest = min(shortest, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        distance += shortest
    MIN = min(MIN, distance)
print(MIN)
