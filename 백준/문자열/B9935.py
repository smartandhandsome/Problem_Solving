"""
https://www.acmicpc.net/problem/9935
"""
st = input()
boom = list(input())
stack = []
for s in st:
    stack.append(s)
    if stack[-len(boom):] == boom:
        del stack[-len(boom):]

print(''.join(stack) if stack else "FRULA")
