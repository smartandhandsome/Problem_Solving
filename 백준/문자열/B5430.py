T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    nums = eval(input())
    p = p.replace("RR", "")
    R_check = False
    error = False
    for c in p:
        if c == 'R':
            R_check = not R_check
        elif c == 'D':
            if len(nums) == 0:
                error =True
                break
            if R_check:
                nums.pop(-1)
            else:
                nums.pop(0)
    if error:
        print('error')
    else:
        if R_check:
            nums.reverse()
        print(str(list(nums)).replace(" ", ""))
