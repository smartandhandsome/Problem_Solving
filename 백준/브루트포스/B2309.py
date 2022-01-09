def check(leng):
    total = sum(leng)
    for i in range(9):
        for j in range(i + 1, 9):
            if total - leng[i] - leng[j] == 100:
                leng.pop(i)
                leng.pop(j-1)
                return sorted(leng)


leng = []
for _ in range(9):
    leng.append(int(input()))
lst = check(leng)

for n in lst:
    print(n)
