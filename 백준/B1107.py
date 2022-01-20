"""
https://www.acmicpc.net/problem/1107
"""
target = int(input())
M = int(input())
now = 100
b_list = []
if M != 0:
    b_list = list(map(int, input().split()))
cnt = abs(now - target)
for channel in range(1000001):
    for c in str(channel):
        if int(c) in b_list:
            break
    else:
        cnt = min(cnt, abs(channel - target) + len(str(channel)))
print(cnt)
