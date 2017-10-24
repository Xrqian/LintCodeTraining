class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        a_ch_dict = {}
        for a_ch in A:
            if a_ch not in a_ch_dict:
                a_ch_dict[a_ch] = 1
            else:
                a_ch_dict[a_ch] += 1
        for b_ch in B:
            if b_ch not in a_ch_dict:
                return False
            elif a_ch_dict.get(b_ch) < 1:
                return False
            else:
                a_ch_dict[b_ch] -= 1
        return True


"""
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是大写字母
(在 A 中出现的 B 字符串里的字符不需要连续或者有序。)
eg:
    A = "ABCD"
    B = "ACD"
    返回 true

    A = "ABCD"
    B = "AABC"
    返回 false
"""
A = "ABCD"
B = "AABC"
s = Solution()
print(s.compareStrings(A, B))
