"""
https://www.acmicpc.net/problem/2630
"""
import sys

input = sys.stdin.readline
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
w_cnt = 0
b_cnt = 0


def solution(a, b, n):
    global w_cnt
    global b_cnt
    color = MAP[a][b]
    for x in range(a, a + n):
        for y in range(b, b + n):
            if color != MAP[x][y]:
                solution(a, b, n // 2)
                solution(a + n // 2, b, n // 2)
                solution(a, b + n // 2, n // 2)
                solution(a + n // 2, b + n // 2, n // 2)
                return

    if color == 1:
        b_cnt += 1
    else:
        w_cnt += 1


solution(0, 0, N)
print(w_cnt)
print(b_cnt)
