import hashlib

s = input()
s = hashlib.sha256(s.encode())
print(s.hexdigest())
print(s.digest())
