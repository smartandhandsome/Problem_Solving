import sys
read = sys.stdin.readline
N, M = map(int, read().split())
dic = {}
for _ in range(N):
    site, password= read().split()
    dic[site] = password
for _ in range(M):
    print(dic[read().rstrip()])
