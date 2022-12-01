n = int(input())
m = sorted(list(map(int, input().split())))
total = 0
for i in m:
    total += i * n
    n -= 1

print(total)
