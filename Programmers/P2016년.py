def solution(a, b):
    answer = ''
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    last = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a):
        day += last[i]
    day += b

    return week[day % 7]

print(solution(5, 24))