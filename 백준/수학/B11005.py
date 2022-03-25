A, B = map(int, input().split())
s = ''
while A > 0:
    temp = A % B
    if temp > 9:
        temp = chr(temp - 10 + ord('A'))
    s += str(temp)
    A //= B

print(s[::-1])