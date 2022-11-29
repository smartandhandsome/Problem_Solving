import sys


def round2(x):
    return int(x) + 1 if x - int(x) >= 0.5 else int(x)


N = int(sys.stdin.readline())

if N == 0:
    print(0)
else:
    rank = sorted([int(sys.stdin.readline()) for _ in range(N)])
    t = round2(N * 0.15)
    print(round2(sum(rank[t:len(rank) - t]) / (N - 2 * t)))