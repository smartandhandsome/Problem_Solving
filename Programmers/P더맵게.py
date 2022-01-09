# 다시 풀어보기
# heapq 배우기

import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
