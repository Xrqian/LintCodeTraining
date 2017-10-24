class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return sum of num1 and num2
    """

    def addStrings(self, num1, num2):
        # write your code here
        num1, num2 = num1[::-1], num2[::-1]
        num1_length, num2_length = len(num1), len(num2)
        if num1_length > num2_length:
            max_length, min_length = num1_length, num2_length
            max_str, min_str = num1, num2
        else:
            max_length, min_length = num2_length, num1_length
            max_str, min_str = num2, num1
        res = ""
        tmp = 0
        for index in range(min_length):
            min_ch = min_str[index]
            max_ch = max_str[index]
            tmp_res = int(min_ch) + int(max_ch) + tmp
            if tmp_res >= 10:
                tmp = 1
                res += str(tmp_res - 10)
            else:
                res += str(tmp_res)
                tmp = 0
        for index in range(min_length, max_length):
            max_ch = max_str[index]
            tmp_res = int(max_ch) + tmp
            if tmp_res >= 10:
                tmp = 1
                res += str(tmp_res - 10)
            else:
                res += str(tmp_res)
                tmp = 0
        if tmp:
            res += str(tmp)
        return res[::-1]


"""
给定两个大数字字符串，返回他们的和
111111111 + 2 = 111111113
"""
s = Solution()
print(s.addStrings("123", "0"))
