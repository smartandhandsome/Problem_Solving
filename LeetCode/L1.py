from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target - nums[i]] = i
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    print(solution.twoSum(nums, target))
