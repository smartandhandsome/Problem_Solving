import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dis = y - x
    max = math.floor(math.sqrt(dis))
    if math.sqrt(dis) == max:
        cnt = max * 2 - 1
    elif dis <= max * max + max:
        cnt = max * 2
    else:
        cnt = max * 2 + 1
    print(cnt)