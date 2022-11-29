N = int(input())
people = []
rank = []
for _ in range(N):
    people.append(tuple(map(int, input().split())))

for me in people:
    my_rank = 1
    for you in people:
        if me[0] < you[0] and me[1] < you[1]:
            my_rank += 1
    rank.append(my_rank)

for r in rank:
    print(r, end=" ")