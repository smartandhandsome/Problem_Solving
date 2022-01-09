import sys
import heapq

input = sys.stdin.readline
left = []
right = []
N = int(input())

for i in range(N):
    num = int(input())
    if len(left) == 0:
        heapq.heappush(left, (-num, num))
    elif len(left) == len(right):
        if num > left[0][1] and num >= right[0]:
            heapq.heappush(right, num)
            n = heapq.heappop(right)
            heapq.heappush(left, (-n, n))
        else:
            heapq.heappush(left, (-num, num))
    elif len(left) > len(right):
        if num < left[0][1]:
            heapq.heappush(left, (-num, num))
            n = heapq.heappop(left)
            heapq.heappush(right, n[1])
        else:
            heapq.heappush(right, num)

    print(left[0][1])
