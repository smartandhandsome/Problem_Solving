N = int(input())

for num in range(1, N + 1):
    numbers = map(int, str(num))
    if (num + sum(numbers)) == N:
        print(num)
        break
    if num == N:
        print(0)
