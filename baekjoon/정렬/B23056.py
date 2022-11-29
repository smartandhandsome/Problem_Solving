N, M = map(int, input().split())
dic = {}
i = 0
while i < 500:
    ban, name = input().split()
    if ban == '0' and name == '0':
        break
    if len(dic.get(ban, [])) >= M or name in dic.keys():
        continue
    dic[ban] = dic.get(ban, []) + [name]
    i += 1

for ban, name in sorted(dic.items(), key=lambda x: (-(int(x[0]) % 2), int(x[0]))):
    for n in sorted(name, key=lambda x: (len(x), x)):
        print(ban, n)
