import sys

S = list(sys.stdin.readline().strip())
stack = []
check = False
for s in S:
    if s == ' ' and not check:
        while stack:
            print(stack.pop(), end="")
        print(end=' ')
    elif s == '<':
        while stack:
            print(stack.pop(), end="")
        check = True
        stack.append(s)
    elif s == '>':
        print(''.join(stack), end='>')
        stack.clear()
        check = False
    else:
        stack.append(s)

while stack:
    print(stack.pop(), end="")
