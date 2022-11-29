a = input().split('-')
for i in range(len(a)):
    j = list(map(int, a[i].split("+")))
    a[i] = sum(j)
total = a[0]
for i in a[1:]:
    total -= int(i)
print(total)
