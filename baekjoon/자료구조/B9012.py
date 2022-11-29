N = int(input())
for _ in range(N):
    st = []
    for i in input():
        try:
            if i == '(':
                st.append(i)
            elif i == ')':
                st.pop()
        except Exception:
            print('NO')
            break
    else:
        if len(st) == 0:
            print('YES')
        else:
            print('NO')
