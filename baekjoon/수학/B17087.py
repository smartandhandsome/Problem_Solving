import math

N, S = map(int, input().split())
locations = list(map(int, input().split()))
GCD_list = []
distances = {abs(S - i) for i in locations}

d = min(distances)

for distance in distances:
    GCD_list.append(math.gcd(d, distance))

print(min(GCD_list))
