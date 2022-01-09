l = input()
s = input()
ans = 0
for i, c in enumerate(s):
    ans += (ord(c) - ord('a') + 1) * (31 ** i)
print(ans % 1234567891)
