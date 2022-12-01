A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))
n = 0
for num in nums:
    m -= 1
    n += num * (A ** m)

answer = []
while n > 0:
    answer.append(n % B)
    n //= B
print(*answer[::-1])