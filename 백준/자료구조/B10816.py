import collections
input()
cards = list(map(int, input().split()))
cards = collections.Counter(cards)
input()
nums = list(map(int, input().split()))

print(" ".join(cards.get(num, 0) for num in nums))
