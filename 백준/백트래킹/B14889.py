import sys

input = sys.stdin.readline
sys.setrecursionlimit(100001)
N = int(input())
s = [[0] * N for _ in range(N)]

for i in range(N):
    s[i] = list(map(int, input().split()))

All = set(i for i in range(N))
team = []
answer = 99999999999


def back(n):
    global answer
    if len(team) == N // 2:
        right = list(All - set(team))
        left_team = 0
        right_team = 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                left_team += s[team[i]][team[j]] + s[team[j]][team[i]]
                right_team += s[right[i]][right[j]] + s[right[j]][right[i]]
        answer = min(answer, abs(left_team - right_team))
        return

    for i in range(n, N):
        if i in team:
            continue
        team.append(i)
        back(i + 1)
        team.pop()


back(0)
print(answer)
