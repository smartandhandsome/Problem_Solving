N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
line = []


def function(x):
    global line
    if x == 0:
        print(*line)
        return
    for num in nums:
        if not line or num >= line[-1]:
            line.append (num)
            function(x - 1)
            line.remove(num)


function(M)
