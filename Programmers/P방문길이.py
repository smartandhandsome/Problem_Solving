def solution(dirs):
    visit = set()
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    x, y = 0, 0
    for d in dirs:
        if d == 'U':
            dx, dy = direction[0]
        elif d == 'D':
            dx, dy = direction[1]
        elif d == 'R':
            dx, dy = direction[2]
        elif d == 'L':
            dx, dy = direction[3]
        a, b = x + dx, y + dy
        if -5 <= a <= 5 and -5 <= b <= 5:
            if (a, b, x, y) not in visit:
                visit.add((x, y, a, b))
            x, y = a, b
    return len(visit)


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
