class Solution:
    """
    @param: : the given number
    @return: whether whether there're two integers
    """

    def checkSumOfSquareNumbers(self, num):
        # write your code here
        import math
        if num < 0:
            return False
        if num == 0:
            return True
        for a in range(int(math.sqrt(num))):
            b = int(math.sqrt(num - a * a))
            if a * a + b * b == num:
                return True
        return False


"""
给一个整数 c, 你需要判断是否存在两个整数 a 和 b 使得 a^2 + b^2 = c.
给出 n = 5
返回 true // 1 * 1 + 2 * 2 = 5
给出 n = -5
返回 false
"""
s = Solution()
print(s.checkSumOfSquareNumbers(400000006))
