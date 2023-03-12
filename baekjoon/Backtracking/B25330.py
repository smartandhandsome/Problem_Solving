"""
5 5
5 3 1 2 4
10 10 10 10 10

5 100
1 1 1 1 1
10 10 10 10 10

5 1
2 2 2 2 2
2 2 2 2 2

20 100000
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 100000
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2

조건: 마을i에서 싸울 경우, 이전에 방문 했던 마을 몬스터 공격력의 합 + 마을i
첫째 줄에 몬스터의 수
N과 시루의 초기 체력 K가 공백으로 구분되어 주어진다.

둘째 줄에 각 마을에 있는 몬스터의 공격력 A_1, A_2,..., A_N이 공백으로 구분되어 주어진다.

셋째 줄에 각 마을에 있는 주민의 수  P_1, P_2, ..., P_N이 공백으로 구분되어 주어진다.

백트래킹? 완탐?
"""

import sys


def backtracking(cur, hp, fatigue, save_citizen):
    global answer
    answer = max(answer, save_citizen)
    if cur == N:
        return
    new_hp = hp - fatigue - binding[cur][0]
    new_fatigue = fatigue + binding[cur][0]
    if new_hp < 0:
        return
    backtracking(cur + 1, hp, fatigue, save_citizen)
    backtracking(cur + 1, new_hp, new_fatigue, save_citizen + binding[cur][1])


input = sys.stdin.readline
N, K = map(int, input().split())
monster_power = list(map(int, input().split()))
citizen = list(map(int, input().split()))
binding = []
for a, b in zip(monster_power, citizen):
    binding.append((a, b))
binding.sort(key=lambda x: (x[0], -x[1]))
answer = 0
backtracking(0, K, 0, 0)
print(answer)
