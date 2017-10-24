class Solution:
    """
    @param: s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        s_dict = {}
        for s_ch in s:
            if s_ch not in s_dict:
                s_dict[s_ch] = 1
            else:
                s_dict[s_ch] += 1
        index = 0
        for s_ch in s:
            if s_dict[s_ch] == 1:
                return index
            index += 1
        return -1


"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""
ss = "{{;;lintcodelintcode}}"
s = Solution()
print(s.firstUniqChar(ss))
