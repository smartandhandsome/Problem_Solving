n = int(input())
A = set(input().split())
m = int(input())
B = input().split()

for b in B:
    if b in A:
        print(1)
    else:
        print(0)
