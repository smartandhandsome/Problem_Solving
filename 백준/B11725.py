from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
dic = defaultdict(list)
parents = [-1] * (N + 1)

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    dic[node1].append(node2)
    dic[node2].append(node1)


def bfs():
    q = deque([1])

    parents[1] = 0
    while q:
        node = q.popleft()
        for c in dic[node]:
            if parents[c] == -1:
                parents[c] = node
                q.append(c)


bfs()
for p in parents[2:]:
    print(p)
