"""
https://www.acmicpc.net/problem/2263
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (N + 1)
for i in range(N):
    position[inorder[i]] = i


def search(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return
    root = postorder[postorder_end]
    print(root, end=" ")
    inorder_root_idx = position[root]
    search(inorder_start, inorder_root_idx - 1, postorder_start, postorder_start + inorder_root_idx - 1 - inorder_start)
    search(inorder_root_idx + 1, inorder_end, postorder_start + inorder_root_idx - 1 - inorder_start + 1,
           postorder_end - 1)


search(0, N - 1, 0, N - 1)
