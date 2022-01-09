N, M = map(int, input().split())

cards = list(map(int, input().split()))
answer = 0
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            cards_sum = cards[i] + cards[j] + cards[k]
            if answer < cards_sum <= M:
                answer = cards_sum

print(answer)
