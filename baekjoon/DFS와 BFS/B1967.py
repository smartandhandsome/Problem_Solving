import sys
sys.setrecursionlimit(10**6)
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    line = list(map(int, input().split()))
    tree[line[0]].append((line[1], line[2]))
    tree[line[1]].append((line[0], line[2]))


def dfs(x, scores):
    for target, score in tree[x]:
        if scores[target] == -1:
            scores[target] = scores[x] + score
            dfs(target, scores)


score_1 = [-1] * (N + 1)
score_1[1] = 0
dfs(1, score_1)
idx = score_1.index(max(score_1))

score_2 = [-1] * (N + 1)
score_2[idx] = 0
dfs(idx, score_2)
print(max(score_2))
