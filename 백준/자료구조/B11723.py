import sys
input = sys.stdin.readline
N = int(input())
SET = set()
for _ in range(N):
    s = input().split()
    if s[0] == 'add':
        SET.add(int(s[1]))
    elif s[0] == 'remove':
        if int(s[1]) in SET:
            SET.remove(int(s[1]))
    elif s[0] == 'check':
        if int(s[1]) in SET:
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        if int(s[1]) in SET:
            SET.remove(int(s[1]))
        else:
            SET.add(int(s[1]))
    elif s[0] == 'all':
        SET = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif s[0] == 'empty':
        SET = set()
