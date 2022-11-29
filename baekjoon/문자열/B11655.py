S = input()

for s in S:
    if s.isalpha():
        if s.isupper():
            s = ord(s) + 13
            if s > ord('Z'):
                s -= 26
        else:
            s = ord(s) + 13
            if s > ord('z'):
                s -= 26
        s = chr(s)
    print(s, end="")
