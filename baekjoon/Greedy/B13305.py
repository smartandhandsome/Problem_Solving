n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
m = price[0]
total = price[0] * dis[0]

for i in range(1, n - 1):
    m = min(price[i], m)
    total += (m * dis[i])

print(total)