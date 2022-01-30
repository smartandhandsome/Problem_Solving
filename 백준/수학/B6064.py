"""
https://www.acmicpc.net/problem/6064
"""
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M, x, y = map(int, input().split())
    flag = -1
    day = x
    while M * N > day:
        if day % M == y or (day % M == 0 and M == y):
            flag = day
            break
        day += N
    print(flag)
