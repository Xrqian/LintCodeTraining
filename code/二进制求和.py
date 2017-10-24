class Solution:
    """
    @param: a: a number
    @param: b: a number
    @return: the result
    """

    def addBinary(self, a, b):
        # write your code here
        a, b = a[::-1], b[::-1]
        a_length, b_length = len(a), len(b)
        if a_length > b_length:
            max_length, min_length = a_length, b_length
            max_str, min_str = a, b
        else:
            max_length, min_length = b_length, a_length
            max_str, min_str = b, a
        res = ""
        tmp = 0
        for index in range(min_length):
            min_ch = min_str[index]
            max_ch = max_str[index]
            tmp_res = int(min_ch) + int(max_ch) + tmp
            if tmp_res >= 2:
                tmp = 1
                res += str(tmp_res - 2)
            else:
                res += str(tmp_res)
                tmp = 0
        for index in range(min_length, max_length):
            max_ch = max_str[index]
            tmp_res = int(max_ch) + tmp
            if tmp_res >= 2:
                tmp = 1
                res += str(tmp_res - 2)
            else:
                res += str(tmp_res)
                tmp = 0
        if tmp:
            res += str(tmp)
        return res[::-1]


"""
给定两个二进制字符串，返回他们的和（用二进制表示)
1 + 3 = 4
^
0 0 1 1
0 0 0 1
-------
0 0 1 0
+
0 0 1 1
0 0 0 1
-------
0 1 0 0
"""
s = Solution()
print(s.addBinary("1110", "1"))
