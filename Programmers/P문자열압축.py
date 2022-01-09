def solution(s):
    st = ""
    length_list = []
    if len(s) == 1:
        return 1
    for cut in range(1, len(s) // 2 + 1):
        count = 1
        temp = s[:cut]
        for i in range(cut, len(s), cut):
            if temp == s[i:i + cut]:
                count += 1
            else:
                if count != 1:
                    st += str(count) + temp
                else:
                    st += temp
                count = 1
                temp = s[i:i + cut]

        if count != 1:
            st += str(count) + temp
        else:
            st += temp

        length_list.append(len(st))
        st = ""

    return min(length_list)


print(solution('a'))
