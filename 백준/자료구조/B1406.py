import sys

s1 = list(sys.stdin.readline().strip())
s2 = []
n = int(sys.stdin.readline())

for _ in range(n):
    o = sys.stdin.readline().strip()
    if o[0] == 'L' and s1:
        s2.append(s1.pop())
    elif o[0] == 'D' and s2:
        s1.append(s2.pop())
    elif o[0] == 'B' and s1:
        s1.pop()
    elif o[0] == 'P':
        s1.append(o[2])
print(''.join(s1 + list(reversed(s2))))
