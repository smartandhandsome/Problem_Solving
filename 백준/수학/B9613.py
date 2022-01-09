import math


T = int(input())

for _ in range(T):
    num_list = list(map(int, input().split()))
    s = 0
    for i in range(1, len(num_list)):
        for j in range(i + 1, len(num_list)):
            s += math.gcd(num_list[i], num_list[j])
    print(s)
