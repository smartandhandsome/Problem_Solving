from collections import deque

A, B = map(int, input().split())
ans = -1
queue = deque([(A, 1)])
while queue:
    (num, cnt) = queue.popleft()
    if num == B:
        ans = cnt
        break
    if num * 2 <= B:
        queue.append((num * 2, cnt + 1))
    if num * 10 + 1 <= B:
        queue.append((num * 10 + 1, cnt + 1))

print(ans)
