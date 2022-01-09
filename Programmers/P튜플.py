def solution(s):
    answer = []
    s = eval(s.replace('{', '[').replace('}', ']'))
    for num in sorted(s, key=lambda x: len(x)):
        for n in num:
            if not n in answer:
                answer.append(n)
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
