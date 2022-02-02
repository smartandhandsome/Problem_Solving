from itertools import permutations
N, M = map(int, input().split())
nums = list(map(int, input().split()))
per = permutations(sorted(nums), M)
for p in per:
    print(*p)