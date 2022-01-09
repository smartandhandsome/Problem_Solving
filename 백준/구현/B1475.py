nums = input()
check = [0] * 10
cnt = 1
for num in nums:
    num = int(num)
    if check[num] == cnt:
        if num == 6 and check[9] < cnt:
            check[9] += 1
        elif num == 9 and check[6] < cnt:
            check[6] += 1
        else:
            cnt += 1
            check[num] += 1
    else:
        check[num] += 1

print(cnt)
