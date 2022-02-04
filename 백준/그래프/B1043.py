"""
반례
6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6
"""

N, M = map(int, input().split())
known_people = set(map(int, input().split()[1:]))

parties = []
total = []
for k in range(M):
    parties.append(set(map(int, input().split()[1:])))
    total.append(1)
for _ in range(M):
    for i, party in enumerate(parties):
        if party & known_people:
            total[i] = 0
            known_people = party | known_people
print(sum(total))