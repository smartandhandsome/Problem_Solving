class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = []
        if numRows == 1:
            return s
        else:
            for i in range(numRows):
                lst.append([])

            cnt = 0
            x, a = 0, 1
            lst[0].append(s[0])

            for c in s[1:]:
                x += a
                lst[x].append(c)
                cnt += 1

                if cnt == numRows - 1:
                    a *= -1
                    cnt = 0
            s = ""
            for l in lst:
                s += ''.join(l)
            return s