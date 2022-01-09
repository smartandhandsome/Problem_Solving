def solution(nums):
    answer = 0
    N = len(nums)
    se = set(nums)
    if len(se) > (N / 2):
        return N / 2
    else:
        return len(se)
