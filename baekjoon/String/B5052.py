import sys


def check(b):
    b.sort()
    for i in range(1, len(b)):
        if b[i - 1] == b[i][:len(b[i - 1])]:
            return False
    return True


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    book = []
    for __ in range(N):
        book.append(sys.stdin.readline().strip())

    if check(book):
        print('YES')
    else:
        print('NO')
