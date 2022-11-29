import sys

sys.setrecursionlimit(10 ** 6)


def hanoi(start, via, end, n):
    if n == 1:
        print(start, end)
        return

    hanoi(start, end, via, n - 1)
    print(start, end)
    hanoi(via, start, end, n - 1)


N = int(input())

print(2 ** N - 1)
hanoi(1, 2, 3, N)
