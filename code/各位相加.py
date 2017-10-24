class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        # write your code here
        while num >= 10:
            tmp, res = num, 0
            while tmp:
                res += tmp % 10
                tmp = int(tmp / 10)
            num = res
        return num


"""
给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。
38
3 + 8 = 11
1 + 1 = 2
2
"""
s = Solution()
print(s.addDigits(38))
