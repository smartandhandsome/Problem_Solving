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