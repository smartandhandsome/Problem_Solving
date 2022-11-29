N = int(input())
nums = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(N)]
for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)