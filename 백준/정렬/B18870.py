import sys

input = sys.stdin.readline
N = int(input().strip())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))

dic = {sorted_nums[i]: i for i in range(len(sorted_nums))}

for num in nums:
    print(dic[num], end=" ")