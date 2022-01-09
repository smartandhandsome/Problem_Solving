import sys

input = sys.stdin.readline

c = 1000000

check = [True] * c

for i in range(2, int(c ** 0.6)):
    if check[i]:
        for j in range(i * 2, c, i):
            if check[j]:
                check[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n):
        if check[i]:
            if check[n - i]:
                print(f'{n} = {i} + {n - i}')
                break
