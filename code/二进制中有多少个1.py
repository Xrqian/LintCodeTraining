class Solution:
    """
    @param: num: An integer
    @return: An integer
    """

    def countOnes(self, num):
        # write your code here
        import ctypes
        res = 0
        while num:
            res += 1
            num = ctypes.c_int32(num).value & ctypes.c_int32(num - 1).value
        return res


"""
计算在一个 32 位的整数的二进制表示中有多少个 1.
eg:
    给定 32 (100000)，返回 1

    给定 5 (101)，返回 2

    给定 1023 (1111111111)，返回 10

分析:
    n & (n -1) 去掉最低位的1
    -----------------------------------------
    8  1000
                8 & 7 = 0000 = 0
    7  0111
    -----------------------------------------
    15 1111
                15 & 14 = 1110 = 14
    14 1110
    -----------------------------------------
    n的二进制        例: 100010001010
    n-1 = n + (-1)      100010001010
                                   +
                        111111111111 （1的补码）
                        100010001001  (n-1的原码)
    得出结论 n & (n - 1) 会去掉 n 的最低位的1
"""
s = Solution()
print(s.countOnes(1023))
