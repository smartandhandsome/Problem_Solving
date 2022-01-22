"""
https://www.acmicpc.net/submit/5525
"""
N = int(input())
S_len = int(input())
S = input()
P = 'IO' * N + 'I'
check = 0
cnt, idx = 0, 1

while idx < S_len - 1:
    if S[idx - 1] + S[idx] + S[idx + 1] == 'IOI':
        idx += 1
        check += 1
        if check == N:
            cnt += 1
            check -= 1
    else:
        check = 0
    idx += 1
print(cnt)
