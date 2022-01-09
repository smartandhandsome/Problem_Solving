bars = list(input())
queue = []
count = 0
for i in range(len(bars)):
    if bars[i] == '(':
        if bars[i + 1] != ')':
            count += 1
        queue.append('(')
    else:
        queue.pop()
        if bars[i - 1] == '(':
            count += len(queue)

print(count)
