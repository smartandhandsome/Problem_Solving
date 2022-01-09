# sys.stdin.readline 쓰는 습관

from collections import Counter
from sys import stdin

input = stdin.readline
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
print(f"{sum(num_list) / N:.0f}")
print(num_list[N // 2])
cnt = Counter(num_list).most_common()
if N > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(num_list[N - 1] - num_list[0])
