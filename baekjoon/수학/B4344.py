C = int(input())

for _ in range(C):
    l = list(map(int, input().split()))
    aver = sum(l[1:]) / l[0]
    count = 0
    for p in l[1:]:
        if aver < p:
            count += 1
    print("{0:0.3f}%".format(count/l[0] * 100))

