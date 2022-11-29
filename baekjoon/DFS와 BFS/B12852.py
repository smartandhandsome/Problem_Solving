from collections import deque

N = int(input())
queue = deque()
queue.append([N])
while queue:
    nums = queue.popleft()
    num = nums[-1]
    if num == 1:
        print(len(nums) - 1)
        print(*nums)
        break
    if num % 3 == 0:
        queue.append(nums + [num // 3])
    if num % 2 == 0:
        queue.append(nums + [num // 2])
    queue.append(nums + [num - 1])
