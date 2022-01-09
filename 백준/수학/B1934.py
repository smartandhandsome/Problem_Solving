import sys


def GCD(X, Y):
    return GCD(Y, X % Y) if Y else X


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    A, B = max(A, B), min(A, B)
    x = GCD(A, B)
    print((A * B) // x)
