import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    num = int(input())
    clothes = []
    for i in range(num):
        name, category = input().split()
        clothes.append(category)
    cnt = 1
    cnt_clothes = Counter(clothes)
    for c in cnt_clothes:
        cnt *= cnt_clothes[c] + 1
    print(cnt - 1)
