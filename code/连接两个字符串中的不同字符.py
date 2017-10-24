class Solution:
    """
    @param: : the 1st string
    @param: : the 2nd string
    @return: uncommon characters of given strings
    """

    def concatenetedString(self, s1, s2):
        # write your code here
        res = ""
        for s1_ch in s1:
            if s1_ch not in s2:
                res += s1_ch
        for s2_ch in s2:
            if s2_ch not in s1:
                res += s2_ch
        return res


"""
给出两个字符串, 你需要修改第一个字符串，将所有与第二个字符串中相同的字符删除, 并且第二个字符串中不同的字符与第一个字符串的不同字符连接
eg:
    s1 = aacdb
    s2 = gafd
    返回 cbgf

    s1 = abcs
    s2 = cxzca;
    返回 bsxz
"""
s1 = "abcs"
s2 = "cxzca"
s = Solution()
print(s.concatenetedString(s1, s2))
