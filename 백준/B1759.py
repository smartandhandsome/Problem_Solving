from itertools import combinations

L, C = map(int, input().split())
chars = sorted(list(input().split()))
com = combinations(chars, L)
for c in com:
    vowels = 0
    consonants = 0
    if 'a' in c:
        vowels += 1
    if 'e' in c:
        vowels += 1
    if 'i' in c:
        vowels += 1
    if 'o' in c:
        vowels += 1
    if 'u' in c:
        vowels += 1
    consonants = len(c) - vowels
    if vowels >= 1 and consonants >= 2:
        print(''.join(c))
