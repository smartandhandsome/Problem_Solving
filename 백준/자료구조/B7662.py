"""
https://www.acmicpc.net/problem/7662
"""
import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    max_Q, min_Q = [], []
    k = int(sys.stdin.readline())
    check = [False] * k
    for key in range(k):
        cmd, n = sys.stdin.readline().split()
        if cmd == 'I':
            n = int(n)
            heapq.heappush(max_Q, (-n, key))
            heapq.heappush(min_Q, (n, key))
            check[key] = True
        elif cmd == 'D':
            n = int(n)
            if n == 1:
                while max_Q and not check[max_Q[0][1]]:
                    heapq.heappop(max_Q)
                if max_Q:
                    check[heapq.heappop(max_Q)[1]] = False
            elif n == -1:
                while min_Q and not check[min_Q[0][1]]:
                    heapq.heappop(min_Q)
                if min_Q:
                    check[heapq.heappop(min_Q)[1]] = False
    while max_Q and not check[max_Q[0][1]]:
        heapq.heappop(max_Q)
    while min_Q and not check[min_Q[0][1]]:
        heapq.heappop(min_Q)
    if min_Q and max_Q:
        print(-max_Q[0][0], min_Q[0][0])
    else:
        print('EMPTY')
