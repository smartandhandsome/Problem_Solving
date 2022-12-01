N = int(input())
s = []
for _ in range(N):
    f, e = map(int, input().split())
    s.append([f, e])
s = sorted(s, key=lambda x: x[0])
s = sorted(s, key=lambda x: x[1])

count = 0
time = 0

for i, j in s:
    if i >= time:
        time = j
        count += 1

print(count)
