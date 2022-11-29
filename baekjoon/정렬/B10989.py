import sys

N = int(sys.stdin.readline())
numbers = [0] * 10001
for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            sys.stdout.write(str(i) + "\n")
