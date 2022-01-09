def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


input()

numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if isPrime(num):
        count += 1
print(count)
