"""
https://www.acmicpc.net/problem/2096
"""
import sys

input = sys.stdin.readline
N = int(input())

for i in range(N):
    a, b, c = map(int, input().split())
    if i != 0:
        a_max = a + max(MAX[0], MAX[1])
        a_min = a + min(MIN[0], MIN[1])
        b_max = b + max(MAX[0], MAX[1], MAX[2])
        b_min = b + min(MIN[0], MIN[1], MIN[2])
        c_max = c + max(MAX[1], MAX[2])
        c_min = c + min(MIN[1], MIN[2])
        MAX = [a_max, b_max, c_max]
        MIN = [a_min, b_min, c_min]
    else:
        MAX = [a, b, c]
        MIN = [a, b, c]
print(max(MAX), min(MIN))
