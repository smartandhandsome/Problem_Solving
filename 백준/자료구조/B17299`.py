from collections import Counter
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
cnt = Counter(nums)
stack = []
answer = [-1 for _ in range(N)]
for i in range(len(nums)):
    while stack and cnt[nums[stack[-1]]] < cnt[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)
print(*answer)
