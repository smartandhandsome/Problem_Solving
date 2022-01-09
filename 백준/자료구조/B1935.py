N = int(input())
s = input()
nums = []
for _ in range(N):
    nums.append(int(input()))
stack = []
for c in s:
    if c == '+' or c == '-' or c == '*' or c == '/':
        B = stack.pop()
        A = stack.pop()
        if c == '+':
            stack.append(A + B)
        elif c == '-':
            stack.append(A - B)
        elif c == '*':
            stack.append(A * B)
        elif c == '/':
            stack.append(A / B)
    else:
        stack.append(nums[ord(c) - ord('A')])
print(f'{stack.pop():.2f}')
