N = input()
nums = []
for num in N:
    nums.append(int(num))
nums.sort(reverse=True)
for n in nums:
    print(n,end="")