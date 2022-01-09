N = int(input())
dic = {}
for i in range(N):
    W, H = map(int, input().split())
    dic[i + 1] = W ** 2 + H ** 2
dic = sorted(dic.items(), key=lambda x: [-x[1], x[0]])
for i in dic:
    print(i[0])
