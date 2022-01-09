import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    lst.append((age, name))

lst = sorted(lst, key=lambda x: x[0])

for age, name in lst:
    print(age, name)
