from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
q = deque()

for _ in range(T):
    command = input().rstrip()
    if command == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif command == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    else:
        command, num = command.split()
        q.append(int(num))
