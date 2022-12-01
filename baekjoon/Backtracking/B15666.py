N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
buf_list = []


def backtracking(x, idx, buf):
    if x == 0:
        buf_list.append(tuple(buf))
        return
    for i in range(idx, len(nums)):
        backtracking(x - 1, i, buf + [nums[i]])


backtracking(M, 0, [])
for buf in buf_list:
    print(*buf)
