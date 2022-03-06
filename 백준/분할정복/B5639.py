"""
https://www.acmicpc.net/problem/5639
"""
import sys

sys.setrecursionlimit(10 ** 6)
tree = []
while True:
    try:
        node = int(input())
    except EOFError:
        break
    tree.append(node)


def solution(start, end):
    if start > end:
        return
    root = tree[start]
    partition = end + 1

    for i in range(start + 1, end + 1):
        if root < tree[i]:
            partition = i
            break

    solution(start + 1, partition - 1)
    solution(partition, end)
    print(root)


solution(0, len(tree) - 1)
