class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        # 递归
        # if n <= 0:
        #     return -1
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # 循环
        if n < 0:
            return -1
        elif 0 <= n <= 2:
            return n
        else:
            a, b, res = 1, 2, 3
            for x in range(2, n):
                res = a + b
                a, b = b, res
            return res


"""
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
eg：
    n = 3
    1 + 1 + 1 = 1 + 2 = 2 + 1 = 3，共有3种不同的方法
return:
    3

分析：
    整数拆分问题
    n = (n - 1) + 1
    n = (n - 2) + 2
    climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)
    递归：
        if n == 0:
            return 0
        if n == 1:
            return 1
        if  n == 2:
            return 2
    模拟：
        c(1) = 1
            1
        c(2) = 2
            1 + 1
            2
        c(3) = c(2) + c(1) = 1 + 2 = 3
            1 + 1 + 1
            1 + 2
            2 + 1
        c(4) = c(3) + c(2) = 2 * c(2) + c(1) = 5
            1 + 1 + 1 + 1
            1 + 2 + 1
            1 + 1 + 2
            2 + 1 + 1
            2 + 2
        c(5) = c(4) + c(3) = 3 * c(2) + 2 * c(1) = 8
            1 + 1 + 1 + 1 + 1
            1 + 1 + 1 + 2
            1 + 1 + 2 + 1
            1 + 2 + 1 + 1
            2 + 1 + 1 + 1
            1 + 2 + 2
            2 + 1 + 2
            2 + 2 + 1
"""
s = Solution()
print(s.climbStairs(4))
