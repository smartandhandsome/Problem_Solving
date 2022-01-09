N, M = map(int, input().split())
nums = []


def back(idx):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(idx, N + 1):
        nums.append(i)
        back(i)
        nums.pop()


back(1)
