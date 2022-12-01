N, M = map(int, input().split())
nums = []


def back():
    if len(nums) == M:
        print(*nums)
        return

    for i in range(1, N + 1):
        nums.append(i)
        back()
        nums.pop()


back()
