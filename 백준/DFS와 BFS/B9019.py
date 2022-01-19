"""
https://www.acmicpc.net/problem/9019
"""
from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    tracking = [()] * 10000
    queue = deque()
    queue.append(A)
    while queue:
        n = queue.popleft()
        if n == B:
            num, cmd = tracking[n]
            ans = cmd
            while num != A:
                num, cmd = tracking[num]
                ans += cmd
            print(ans[::-1])
            break
        for cmd in ('D', 'S', 'L', 'R'):
            num = n
            if cmd == 'D':
                num = num * 2 % 10000
            elif cmd == 'S':
                if num == 0:
                    num = 9999
                else:
                    num -= 1
            else:
                d1 = num // 1000
                d2 = num % 1000 // 100
                d3 = num % 100 // 10
                d4 = num % 10
                if cmd == 'L':
                    num = d2 * 1000 + d3 * 100 + d4 * 10 + d1
                elif cmd == 'R':
                    num = d4 * 1000 + d1 * 100 + d2 * 10 + d3
            if not tracking[num]:
                queue.append(num)
                tracking[num] = (n, cmd)
