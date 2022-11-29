N, B = input().split()
B = int(B)

power = 0
total = 0

for n in N[::-1]:
    if n.isalpha():
        n = ord(n) - ord('A') + 10
    else:
        n = int(n)
    total += n * (B ** power)
    power += 1
print(total)
