def first():
    from collections import Counter

    S = input()
    cnt = Counter(S)

    for i in range(ord('a'), ord('z') + 1):
        print(cnt.get(chr(i), 0), end=" ")


def second():
    nums = [0] * 26
    for c in input():
        nums[ord(c) - ord('a')] += 1
    print(*nums)
