n = int(input())

for _ in range(n):
    s = input().split()
    stack = []
    for c in s:
        for ch in c:
            stack.append(ch)
        while len(stack) > 0:
            print(stack.pop(), end="")
        print(end=" ")
    print()
