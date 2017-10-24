class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here
        # 递归
        # return a if not b else aplusb(a ^ b, (a & b) << 1)
        # 循环
        import ctypes
        while b:
            tmp = ctypes.c_int32(a & b).value << 1
            res = a ^ b
            a = res
            b = tmp
        else:
            return a


s = Solution()
print(s.aplusb(8, -4))

"""
^
0 0 = 0
0 1 = 1
1 0 = 1
1 1 = 0
&
0 0 = 0
0 1 = 0
1 0 = 0
1 1 = 1
eg:
2 + 3 = 5
0 0 1 0
0 0 1 1
-------
0 1 0 1
2 ^ 3 = 0 0 0 1 = 1
2 & 3 = 0 0 1 0 = 2 (向左进一位，加法进位)
plus(2, 3) = plus(2 ^ 3, (2 & 3) << 1) = plus(1, 4)
plus(1 ,4) = plus(5, 0)
递归，确定递归出口
"""
