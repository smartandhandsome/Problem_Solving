class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i in range(len(s)):
            temp = []
            for c in s[i:]:
                if c in temp:
                    break
                temp.append(c)
            if longest < len(temp):
                longest = len(temp)
            temp.clear()

        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
